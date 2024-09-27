from langchain.text_splitter import RecursiveCharacterTextSplitter
from openai import OpenAI
import json
import asyncio
import argparse
from tqdm.asyncio import tqdm_asyncio
import re
from tqdm import tqdm
import os
def get_response1(text, system_setting="你是一个资深心理学家。你正在为你的学生出一份心理学考试的考卷。"):
    client = OpenAI(
        api_key=""
    )
    
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{'role': 'system', 'content': system_setting},
                  {'role': 'user', 'content': text}],
        temperature=1,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        response_format={
            "type": "text"
        }
        )
    return response.choices[0].message.content

def get_response2(text, system_setting="你是一个改写专家，你将根据任务要求对输入文本进行改写。"):
    client = OpenAI(
        api_key="", # 如果您没有配置环境变量，请在此处用您的API Key进行替换
        base_url="",  # 填写DashScope服务的base_url
    )
    response = client.chat.completions.create(
        model="qwen-max",
        messages=[{'role': 'system', 'content': system_setting},
                  {'role': 'user', 'content': text}],
        max_tokens=512,
        temperature=0.7,
        top_p=0.7,
        )
    return response.choices[0].message.content

def remove_control_characters(content):
    
    cleaned_content = re.sub(r"[\x00-\x1F\x7F]"," ",content)
    return cleaned_content

async def get_qa_js(text, prompt_path, ori_qa_num, retry_num=4):
    prompt=""
    with open(prompt_path, "r", encoding='utf-8') as f:
        prompt=f.read()
    input=prompt.replace('{text}', text)
    input=prompt.replace('{num}', str(ori_qa_num))
    qa_str=get_response1(input)
    qa_js={}
    flag=False
    for i in range(retry_num):
        try:
            qa_str=qa_str.strip()
            # if((not qa_str.startswith("[")) and qa_str.endswith("```")):
            #     qa_str=qa_str[qa_str.find("["):qa_str.find("]")+1]#去掉```json开头和```结尾
            # if not (qa_str.endswith("]")):#通常是后面没有]
            #     print(rf"try to fix qas in wrong json format:\n{qa_str}")
            #     if (qa_str.endswith(",")):
            #         qa_str=qa_str+"]"
            #     elif (qa_str.endswith("}")):
            #         qa_str=qa_str+",]"
            #     else:
            #         qa_str=qa_str+"},]"
            #     print(rf"qas in wrong json format after fixing:\n{qa_str}")
            qa_js=json.loads(qa_str[qa_str.find("["):qa_str.find("]")+1])
            flag=True
            break
        except:
            qa_str=get_response1(input)
    if(flag==False):
        print(f"生成的qa结果格式错误：{qa_str}")
        qa_str=""
        qa_js={}
    # else:
    #     qa_str=qa_str[qa_str.find("[")+1:qa_str.find("]")]+",\n"#后面合并多个qa_str要用到
    return qa_js

async def get_more_q_js(origin_q, prompt_path, retry_num=4):
    prompt=""
    with open(prompt_path,"r",encoding="utf-8") as f:
        prompt=f.read()
    input=prompt.replace("{text}", origin_q)
    i_str=get_response2(input)
    i_js=[]
    flag=False
    for i in range(retry_num):
        try:
            i_js=json.loads(i_str[i_str.find("["):i_str.find("]")+1])
            if not all(isinstance(item, str) for item in i_js):
                raise ValueError("get_i_js过程中得到的list里面并不是都装着str对象")
            flag=True
            break
        except:
            i_str=get_response2(input)
    if(flag==False):
        print(f"生成更多指令的结果格式错误：{i_str}")
        i_str=""
        i_js=[]
    i_js.insert(0, origin_q)
    return i_js

def add_prefix(new_instructions, instruction_prefix):
    for i in range(len(new_instructions)):
        try:
            new_instructions[i]=instruction_prefix+new_instructions[i]
        except:
            print(f"wrong new_instruction:{new_instructions}")
            print(f"wrong new_instruction[{i}]:{new_instructions[i]}")
    return new_instructions

def adapt_to_training_format(input_path, output_path):
    #把方便read形式的数据转成train需要的格式储存
    ori_js={}
    with open(input_path, "r", encoding="utf-8") as f:
        ori_str=f.read()
    try:    
        ori_js=json.loads(ori_str)
    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")
        print(f"Error at line {e.lineno} column {e.colno} (char {e.pos})")
        print(f"Context: {ori_str[max(e.pos-40, 0):e.pos]}{'[ERROR]'}{ori_str[e.pos:e.pos+40]}")
        raise

    rs=[]
    for i in range(len(ori_js)):
        single_rs=ori_js[i]["rs"]
        for j in range(len(single_rs)):
            insturctions=single_rs[j]["instruction"]
            output=single_rs[j]["output"]
            input=single_rs[j]["input"]
            temp=[]
            for k in range(len(insturctions)):
                temp.append({"instruction":insturctions[k], "input":input, "output":output})
            rs.extend(temp)

    with open(output_path, "w", encoding="utf-8") as f: 
        f.write(json.dumps(rs,ensure_ascii=False,indent=4))
    return 

async def get_dataset(input_file_path, output_file_path_read, output_file_path_train, q_a_prompt_path, m_q_prompt_path, instruction_prefix):
    print("go!")
    
    texts=[]
    input_filenames=[]
    filenames=os.listdir(input_file_path)    
    for i in range(len(filenames)):
        if(filenames[i].startswith("input")):
            input_filenames.append(filenames[i])
            with open(os.path.join(input_file_path, filenames[i]), "r", encoding="utf-8") as f:
                texts.append(f.read())
    
    tasks=[]
    for i in range(len(texts)):
        texts[i]=remove_control_characters(texts[i])
        ori_qa_num=len(texts[i])//100
        tasks.append(asyncio.create_task(get_qa_js(texts[i], q_a_prompt_path, ori_qa_num)))
        #print(texts[i])
    res_list=await tqdm_asyncio.gather(*tasks)
    
    print("extend dataset!")
    res_to_write=""
    
    for i,text in tqdm(enumerate(texts), total=len(texts)):
        if(res_list[i]!={}):
            tasks2=[]
            for j in range(len(res_list[i])):
                tasks2.append(asyncio.create_task(get_more_q_js(res_list[i][j]["instruction"], m_q_prompt_path)))
            res2_list=await asyncio.gather(*tasks2)

            for j in range(len(res2_list)):
                new_instructions=res2_list[j]
                new_instructions=add_prefix(new_instructions, instruction_prefix)
                res_list[i][j]["instruction"]=new_instructions

                
            rs={"related_text":text, "rs":res_list[i]}
            with open(os.path.join(output_file_path_read, input_filenames[i].replace("input","output_read")), "w", encoding="utf-8") as f_r:
                f_r.write(json.dumps(rs,ensure_ascii=False,indent=4))
            #res_to_write=res_to_write+json.dumps(rs,ensure_ascii=False,indent=4).replace("\\n","\n").replace("\\\"","\"").replace("\\t","\t")+"\n,\n"
        else:
            print(f"生成qa失败，文件名为:{input_filenames[i]}")
            continue
    
    
    # #下面写入的数据以方便机器train的形式组织

    for i in range(len(input_filenames)):
        output_read_file_path=os.path.join(output_file_path_read, input_filenames[i].replace("input","output_read"))
        output_train_file_path=os.path.join(output_file_path_train, input_filenames[i].replace("input","output_train"))
        adapt_to_training_format(output_read_file_path, output_train_file_path)
    
    

if __name__=="__main__":    
    parser = argparse.ArgumentParser()
    parser.add_argument('-output_file_read', help='输出路径(一个目录)，以方便查看的形式组合数据', default="./output_read/")
    parser.add_argument('-output_file_train', help='输出路径(一个目录)，以方便训练的形式组合数据', default="./output_train/")
    parser.add_argument('-input_file', help='输入路径', default="./input/")
    parser.add_argument('-prompt_path1', help="prompt模板所在的地方", default="./get_qas_prompt_theory_auto.txt")
    parser.add_argument('-prompt_path2', help="拓展指令的prompt模板所在的地方", default="./get_more_q_prompt1.txt")
    parser.add_argument('-instruction_prefix', help="指令前缀", default="你是一个心理学专家。请回答以下问题或完成以下任务：")
    args = parser.parse_args()
    input_file_path=args.input_file
    output_file_path_read=args.output_file_read
    output_file_path_train=args.output_file_train
    prompt_path1=args.prompt_path1
    prompt_path2=args.prompt_path2
    instruction_prefix=args.instruction_prefix
    
    asyncio.run(get_dataset(input_file_path,output_file_path_read,output_file_path_train,prompt_path1, prompt_path2, instruction_prefix))
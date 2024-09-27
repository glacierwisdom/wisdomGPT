"""
使用oneapi与llm对话
"""
from openai import OpenAI
import os

def get_response(text, system_setting="You are a helpful assistant."):
    client = OpenAI(
        api_key="your api key", 
        base_url="your base url",  
    )
    completion = client.chat.completions.create(
        model="qwen-plus",
        messages=[{'role': 'system', 'content': system_setting},
                  {'role': 'user', 'content': text}]
        )
    return completion.model_dump_json()

#llm输出的json有时候会抽风，格式会错，以下这个函数是用来修改格式的,text是要修改的输出，num是最大的修改次数
def fix_json_format_template(text, num=5):
    fix_json_format_template="./prompt_template/fix_json_format_template.txt"
    prompt=""
    completion=""
    result={"num":num, "is_fix":"no", "result":text}
    flag=False
    for i in range(num):
        try:
            prompt=generate_prompt(text, fix_json_format_template)
            completion=get_response(prompt)
            content=json.loads(completion)["choices"][0]["message"]["content"]
            #print(content[content.find("{"):content.rfind("}")+1])
            str_rs=""
            idx_1=content.find("{")
            idx_2=content.find("[")
            if((idx_1!=-1 and idx_2==-1) or (idx_1!=-1 and idx_2!=-1 and idx_1<idx_2)):
                str_rs=content[idx_1:content.rfind("}")+1]
            else:
                str_rs=content[idx_2:content.rfind("]")+1]
            result["num"]=i+1
            result["is_fix"]="yes"
            result["result"]=str_rs
            flag=True
        except:
            flag=False
        if(flag):
            break
        else:
            continue
    return result
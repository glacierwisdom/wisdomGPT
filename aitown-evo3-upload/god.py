from memory1 import Memory
from global_method import *
from llm import *
import json
from langchain_core.documents import Document
from resident_agent import ResidentAgent
from doctor_agent import DoctorAgent
class GodAgent():
    def __init__(self, prompt_template, memory_path):
        self.prompt_template=prompt_template
        self.good_memory=Memory(f"{memory_path}/god/good_memory", "good_memory")
        self.bad_memory=Memory(f"{memory_path}/god/bad_memory", "bad_memory")
        self.generate_portrait_god_template=prompt_template+"/generate_resident_portrait_god_template.txt"
        self.generate_god_suggestion_template=prompt_template+"/generate_god_suggestion_template.txt"
        self.portrait={}
        self.generate_resident_portrait_god_template=prompt_template+"/generate_resident_portrait_god_template.txt"
        self.update_god_memory_bad_template=prompt_template+"/update_god_memory_bad.txt"
        self.update_god_memory_good_template=prompt_template+"/update_god_memory_good.txt"
    #n个医生对病人的画像 n个医生agent的建议 好记忆 坏记忆 topn===》选择哪几个+理由 终极理由
    def generate_portrait_god(self, resident, recent_actions, reason_need_help, question, reply, doctor_portraits):
        parameters=[resident.get_basic_description(), recent_actions, reason_need_help, question, reply, doctor_portraits]
        prompt=generate_prompt(parameters, self.generate_resident_portrait_god_template)
        content=json.loads(get_response(prompt))["choices"][0]["message"]["content"]
        self.portrait[resident.name]=content
        return content
        
    def generate_god_suggestion(self, resident, doctor_suggestion, reference_num=1):
        portrait="暂无"
        if(resident.name in self.portrait.keys()):
            portrait=self.portrait[resident.name]
        good_memory=self.good_memory.query(portrait)
        bad_memory=self.bad_memory.query(portrait)
        parameters=[doctor_suggestion, portrait, good_memory, bad_memory, reference_num]
        prompt=generate_prompt(parameters, self.generate_god_suggestion_template)
        #print("prompt:\n",prompt)
        flag=False
        rs={}
        for i in range(5):
            try:
                content=json.loads(get_response(prompt))["choices"][0]["message"]["content"]
                content=content[content.find("{"):content.rfind("}")+1]
                rs=json.loads(content)
                flag=True
            except:
                flag=False
            if(flag):
                break
            else:
                continue
        if(not flag):
            print(f"generate_god_suggestion返回格式出错，debug:\n{rs}")
        return rs

    
    def update_memory(self, time_str, resident, doctor_suggestion_list, god_reference, god_suggestion, accept, perma_pre_simple, mood_pre, perma_post_simple, mood_post):
        '''
        更新医生memory
        '''
        parameters=[time_str, resident.get_basic_description(), self.portrait[resident.name], doctor_suggestion_list, god_reference, god_suggestion, accept, perma_pre_simple, mood_pre, perma_post_simple, mood_post]
        if(accept["choice"]=="yes"):
            template_path=self.update_god_memory_good_template
            memory_text=generate_prompt(parameters,template_path)
            #print(f"医生agent增加的好的干预记忆：\n{memory_text}")
            memory_d=[Document(page_content=memory_text, metadata={"source":"good_memory", "timestamp":time_str})]
            self.good_memory.add(memory_d)
        #elif(accept["choice"]=="no"):
        else:#会有no和yes_but_not_best,都算到坏记忆里面
            template_path=self.update_god_memory_bad_template
            memory_text=generate_prompt(parameters,template_path)
            #print(f"医生agent增加的坏的干预记忆：\n{memory_text}")
            memory_d=[Document(page_content=memory_text, metadata={"source":"bad_memory", "timestamp":time_str})]
            self.bad_memory.add(memory_d)      
        
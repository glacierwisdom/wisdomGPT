from memory1 import Memory
from global_method import *
from llm import *
import json
from langchain_core.documents import Document
class DoctorAgent():
    def __init__(self, name, age, personality, style, prompt_template, memory_path):
        self.name=name
        self.age=age
        self.personality=personality
        self.style=style
        self.prompt_template=prompt_template
        self.generate_doctor_question_template=prompt_template+"/generate_doctor_question_template.txt"
        self.generate_doctor_suggestion_template=prompt_template+"/generate_doctor_suggestion_template.txt"
        self.generate_resident_portrait_template=prompt_template+"/generate_resident_portrait_template.txt"
        self.good_memory=Memory(f"{memory_path}/{self.name}/good_memory", "good_memory")
        self.bad_memory=Memory(f"{memory_path}/{self.name}/bad_memory", "bad_memory")
        self.resident_portrait={}

    #后面需要细化
    def get_system_setting(self):
        setting=f"""
        你将扮演以下角色：
        名字：{self.name}
        职业：心理医生
        年龄：{self.age}
        性格：{self.personality}
        治疗风格：{self.style}
        你是一个资深的心理医生，接下来你将从{self.style}的角度对来访患者给出建议。
        """
        return setting
        
    def get_portrait_or_default_description(self, resident):
        if(resident.name not in self.resident_portrait.keys()):
            return resident.get_basic_description()
        else:
            return self.resident_portrait[resident.name]
            
    def generate_doctor_question(self, resident):
        agent_description=self.get_portrait_or_default_description(resident)
        recent_actions=resident.recent_actions
        action=resident.recent_actions
        mood=resident.mood
        related_good_memory=self.good_memory.query(agent_description+str(recent_actions)+str(mood))
        related_bad_memory=self.bad_memory.query(agent_description+str(recent_actions)+str(mood))
        parameters=[agent_description, recent_actions, action, related_good_memory, related_bad_memory]
        prompt=generate_prompt(parameters, self.generate_doctor_question_template)
        #print(f"生成的prompts：\n{prompt}")
        system_settting=self.get_system_setting()
        completion=get_response(prompt, self.get_system_setting())
        content=json.loads(completion)["choices"][0]["message"]["content"]
        question=""
        try:
            question_js=json.loads(content[content.find("["):content.rfind("]")+1])
            question=content[content.find("["):content.rfind("]")+1]
        except:
            fix_result=fix_json_format_template(content[content.find("["):content.rfind("]")+1])
            if(fix_result["is_fix"]=="yes"):
                question=fix_result["result"]
                #print(f"修正mood成功，修正次数：{fix_result['num']}\n修正结果：{mood}")
            else:
                print("generate_doctor_question_debug:",content)
                print(f"修正医生生成的问题失败，修正次数：{fix_result['num']}\n问题为空字符")
                question={"1":"","2":""}
        #print(f"question:\n{question}")
        return question
    
    def generate_doctor_suggestion(self, resident, question, reply):
        agent_description=self.get_portrait_or_default_description(resident)
        recent_actions=resident.recent_actions
        action=resident.action
        mood=resident.mood
        #总结画像，改一下下面的query，改成agent基本信息+医生总结的用户画像（由聊天记录和recent_action+旧的画像，主要用新的东西去修改旧的画像。）
        #上帝画像是所有医生做的画像的合集
        related_good_memory=self.good_memory.query(agent_description+str(mood)+str(question)+str(reply))
        related_bad_memory=self.bad_memory.query(agent_description+str(mood)+str(question)+str(reply))
        parameters=[agent_description, recent_actions, action, related_good_memory, related_bad_memory, question, reply]
        prompt=generate_prompt(parameters, self.generate_doctor_suggestion_template)
        #print(f"生成的prompts：\n{prompt}")
        system_settting=self.get_system_setting()
        completion=get_response(prompt, self.get_system_setting())
        content=json.loads(completion)["choices"][0]["message"]["content"]
        suggestion={"suggestion":"", "reason":""}
        try:
            suggestion=json.loads(content[content.find("{"):content.rfind("}")+1])
            #suggestion=content[content.find("{"):content.rfind("}")+1]
        except:
            fix_result=fix_json_format_template(content[content.find("{"):content.rfind("}")+1])
            if(fix_result["is_fix"]=="yes"):
                suggestion=json.loads(fix_result["result"])
                #print(f"修正mood成功，修正次数：{fix_result['num']}\n修正结果：{mood}")
            else:
                print("mood_pre_debug:",content)
                print(f"修正医生生成的问题失败，修正次数：{fix_result['num']}\n生成的建议为空字符")
        #print(f"suggestion:\n{suggestion}")
        return suggestion
        
    def update_memory(self, time_str, resident, question, reply, suggestion, accept, perma_pre_simple, mood_pre, perma_post_simple, mood_post):
        '''
        更新医生memory
        '''
        parameters=[time_str, self.get_portrait_or_default_description(resident), question, reply, suggestion, accept, perma_pre_simple, mood_pre, perma_post_simple, mood_post, resident.recent_actions]
        if(accept["choice"]=="yes"):
            template_path=self.prompt_template+"/update_doctor_memory_good.txt"
            memory_text=generate_prompt(parameters,template_path)
            #print(f"医生agent增加的好的干预记忆：\n{memory_text}")
            memory_d=[Document(page_content=memory_text, metadata={"source":"good_memory", "timestamp":time_str})]
            self.good_memory.add(memory_d)
        elif(accept["choice"]=="no"):
            template_path=self.prompt_template+"/update_doctor_memory_bad.txt"
            memory_text=generate_prompt(parameters,template_path)
            #print(f"医生agent增加的坏的干预记忆：\n{memory_text}")
            memory_d=[Document(page_content=memory_text, metadata={"source":"bad_memory", "timestamp":time_str})]
            self.bad_memory.add(memory_d)

    def generate_resident_portrait(self, resident, recent_actions, reason_need_help, question, reply):
        former_portrait="暂无"
        if(resident.name in self.resident_portrait.keys()):
            former_portrait=self.resident_portrait[resident.name]
        parameters=[resident.get_basic_description(), recent_actions, reason_need_help, question, reply, former_portrait]
        prompt=generate_prompt(parameters, self.generate_resident_portrait_template)
        portrait=json.loads(get_response(prompt, self.get_system_setting()))["choices"][0]["message"]["content"]
        self.resident_portrait[resident.name]=portrait
        return portrait
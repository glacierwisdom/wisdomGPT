from memory1 import Memory
from global_method import *
from llm import *
import json
from openai import OpenAI
from langchain_core.documents import Document
import asyncio

# from chromadb.config import Settings
# from chromadb import PersistentClient
class ResidentAgent:
    def __init__(
        self,
        name,
        age,
        job,
        personality,
        health,
        perma,
        sds,
        sas,
        gwb,
        mood,
        relationship,
        hobby,
        daily_requirement,
        default_plan,
        memory_path,
        prompt_path,
        preference_on_suggestions,
        behavior,
        perma_mean,
        perma_std,
        perma_law,
        max_recent_actions=10,
    ):
        self.name = name
        self.age = age
        self.job = job
        self.personality = personality
        self.health = health
        self.perma = perma
        self.perma_detail = "默认初始perma值"
        self.sds = sds
        self.sas = sas
        self.sds_detail = "初始sds值"
        self.sas_detail = "初始sas值"
        self.gwb = gwb
        self.gwb_detaail = "初始gwb值"
        
        self.mood = mood
        self.relationship = relationship
        self.hobby = hobby
        self.daily_requirement = daily_requirement
        self.default_plan = default_plan
        self.daily_memory = Memory(
            f"{memory_path}/{self.name}/daily_memory", "daily_record"
        )
        self.medical_memory = Memory(
            memory_path + f"/{self.name}/medical_memory", "medical_record"
        )
        self.preference_on_suggestions = preference_on_suggestions
        self.behavior = behavior
        self.perma_mean = perma_mean
        self.perma_std = perma_std
        self.perma_law = perma_law
        self.plan = 0
        self.generate_plan_prompt_path = prompt_path + "/generate_plan_template.txt"
        
        self.generate_perma_prompt_pre_path = (
            prompt_path + "/generate_perma_pre_template.txt"
        )
        self.generate_sds_pre_template_path = (
            prompt_path + "/generate_sds_pre_template.txt"
        )
        self.generate_sas_pre_template_path = (
            prompt_path + "/generate_sas_pre_template.txt"
        )
        self.generate_mood_prompt_pre_path = (
            prompt_path + "/generate_mood_pre_template.txt"
        )
        self.generate_resident_reply_path = (
            prompt_path + "/generate_resident_reply_template.txt"
        )
        self.generate_gwb_pre_template_path = (prompt_path + "/generate_resident_gwb_pre_template.txt")
        self.generate_gwb_with_dialogue_path = prompt_path +"/generate_gwb_with_dialogue_template.txt"
        self.generate_sds_with_dialogue_path = (
            prompt_path + "/generate_sds_with_dialogue_template.txt"
        )
        self.generate_sas_with_dialogue_path = (
            prompt_path + "/generate_sas_with_dialogue_template.txt"
        )
        
        # self.accept_or_not_path = prompt_path+"/accept_or_not_template.txt"#没有设置病人对建议偏好的prompt
        self.accept_or_not_path = (
            prompt_path + "/accept_or_not_template_2.txt"
        )  # 设置了病人对于建议的偏好的prompt
        self.generate_perma_with_dialogue_path = (
            prompt_path + "/generate_perma_with_dialogue_template.txt"
        )
        self.generate_mood_with_dialogue_path = (
            prompt_path + "/generate_mood_with_dialogue_template.txt"
        )
        self.update_memory_path = prompt_path + "/update_resident_memory.txt"
        self.change_plan_path = prompt_path + "/change_plan_template.txt"
        self.generate_action_detail_path = (
            prompt_path + "/generate_action_detail_template.txt"
        )
        self.resident_help_path = prompt_path + "/resident_help_template.txt"
        self.action = {
            "time": "00:00:00",
            "action": "空闲",
            "mood": mood,
            "perma": perma,
        }  # agent当前活动记录，是take_action会更新它，格式：{"time":time_str, "action":action, "mood": self.mood, "perma": self.perma}
        self.today_actions = (
            []
        )  # 用于生成action细节，让居民在生成action细节的时候能回想到今天已经发生的事情，能够让他的表现更加的连贯。
        self.current_doctor_suggestion = "无"
        self.recent_actions = []
        self.max_recent_actions = max_recent_actions

    def add_recent_actions(self, action):
        if len(self.recent_actions) >= self.max_recent_actions:
            self.recent_actions.pop(0)
        self.recent_actions.append(action)

    def reset_recent_actions(self):
        self.recent_actions = []

    def add_today_actions(self, action):
        self.today_actions.append(action)

    def reset_today_actions(self):
        self.today_actions = []

    def get_str_description(self):
        # 居民自己用到的基本信息描述，尽可能包含所有描述
        return f"人名：{self.name}\n年龄：{self.age}\n工作：{self.job}\n性格：{self.personality}\n健康状况：{self.health}\n最近的Perma值：{self.perma}\n最近sds值：{self.sds}\n最近sas值：{self.sas}\n最近gwb值：{self.gwb}\n最近的心情：{self.mood}\n社会关系：{self.relationship}\n爱好：{self.hobby}\n行为模式：{self.behavior}"

    def get_str_description_without_behavior(self):
        # 居民自己用到的基本信息描述，尽可能包含所有描述
        return f"人名：{self.name}\n年龄：{self.age}\n工作：{self.job}\n性格：{self.personality}\n健康状况：{self.health}\n最近的Perma值：{self.perma}\n最近sds值：{self.sds}\n最近sas值：{self.sas}\n最近gwb值：{self.gwb}\n最近的心情：{self.mood}\n社会关系：{self.relationship}\n爱好：{self.hobby}"

    def get_str_description_without_perma_mood(self):
        return f"人名：{self.name}\n年龄：{self.age}\n工作：{self.job}\n性格：{self.personality}\n健康状况：{self.health}\n社会关系：{self.relationship}\n爱好：{self.hobby}"

    def get_basic_description(self):
        # 医生会看到的基本信息
        return f"人名：{self.name}\n年龄：{self.age}\n工作：{self.job}\n性格：{self.personality}\n健康状况：{self.health}\n社会关系：{self.relationship}\n爱好：{self.hobby}"

    def generate_plan(
        self, begin_time, end_time
    ):  # datetime format YYYY-MM-DD HH:MM:SS，
        # 不确定是否要设置时间，这两个参数可以暂时先乱传，如果后面要细化，要动态规划的话，这两个参数就有用，就要把prompt也改了
        last_medical_memory = self.medical_memory.get_last_memory()
        parameters = [
            self.name,
            self.age,
            self.job,
            self.personality,
            self.health,
            self.perma,
            self.mood,
            self.relationship,
            self.hobby,
            self.current_doctor_suggestion,
            self.daily_requirement,
            self.behavior,
        ]
        prompt = generate_prompt(parameters, self.generate_plan_prompt_path)
        # print(f"生成的prompts：\n{prompt}")
        content = json.loads(get_response(prompt))["choices"][0]["message"]["content"]
        js_plan = 0
        # js_plan=json.loads(rs[rs.find("{"):rs.rfind("}")+1])
        try:
            js_plan = json.loads(content[content.find("[") : content.rfind("]") + 1])
            # print(f"生成的plan:\n{js_plan}")
        except:
            fix_result = fix_json_format_template(
                content[content.find("[") : content.rfind("]") + 1]
            )
            if fix_result["is_fix"] == "yes":
                # print(f"修正的plan:\n修正次数{fix_result['num']}\n修正结果：{fix_result['result']}")
                js_plan = fix_result["result"]
            else:
                if self.plan != 0:
                    js_plan = (
                        self.plan
                    )  # 生成失败让他直接执行上前天的计划，后续写完memory把这里改成重复提问让agent修正的做法
                    print(
                        f"修正失败:\n修正次数{fix_result['num']}\n延续前一天计划：{js_plan}"
                    )
                else:
                    js_plan = self.default_plan
                    print(
                        f"修正失败:\n修正次数{fix_result['num']}\n采用默认计划：{js_plan}"
                    )
        self.plan = js_plan
        return js_plan
    
    async def generate_gwb_pre(self, action):
        """
        前测生成gwb，输入当前行动，结合背景得到gwb，可以用于衡量动作的影响
        也可以用于后续听取医生建议后采取行动的gwb预测。
        """
        parameters = [self.get_basic_description(), action]
        prompt = generate_prompt(parameters, self.generate_gwb_pre_template_path)
        content = json.loads(get_response(prompt))["choices"][0]["message"]["content"]
        
        gwb = 0
        js_gwb = 0
        flag=False
        for i in range(3):
            try:
                js_gwb = json.loads(content[content.find("{") : content.rfind("}") + 1])
                flag=True
            except:
                print("重新生成gwb")
                content = json.loads(get_response(prompt))["choices"][0]["message"]["content"]
            if(flag==True):
                break
            else:
                continue    
        if(flag):
            total = 0
            for key in js_gwb.keys():
                total += js_gwb[key]["score"]
            gwb = total
        else:
            print(f"gwb_pre_debug:{content}")
            gwb = 75
            print(
                f"修正失败，修正次数：3\n生成默认的gwb:\n{gwb}"
            )
            js_gwb = {"默认初始gwb值": 75}
        self.gwb = gwb
        gwb_detail = json.dumps(js_gwb, ensure_ascii=False)
        self.gwb_detail = gwb_detail
        return gwb, gwb_detail
    
    async def generate_perma_pre(self, action):
        """
        前测生成perma，输入当前行动，结合背景得到perma，可以用于衡量动作的影响
        也可以用于后续听取医生建议后采取行动的perma预测。
        """
        parameters = [self.get_basic_description(), action]
        prompt = generate_prompt(parameters, self.generate_perma_prompt_pre_path)
        # print(f"生成的prompts：\n{prompt}")
        content = json.loads(get_response(prompt))["choices"][0]["message"]["content"]
        perma = 0
        js_perma = 0
        ###
        flag=False
        for i in range(3):
            try:
                js_perma = json.loads(content[content.find("{") : content.rfind("}") + 1])
                flag=True
            except:
                print("重新生成perma")
                content = json.loads(get_response(prompt))["choices"][0]["message"]["content"]
            if(flag==True):
                break
            else:
                continue    
        if(flag):
            total = 0
            for key in js_perma.keys():
                total += js_perma[key]["score"]
            perma = total / 23
        else:
            print(f"gwb_pre_debug:{content}")
            perma = 5
            print(
                f"修正失败，修正次数：3\n生成默认的perma:\n{perma}"
            )
            js_perma = {"默认初始perma值": 5}
        self.perma = perma
        perma_detail = json.dumps(js_perma, ensure_ascii=False)
        self.perma_detail = perma_detail
        return perma, perma_detail

    async def generate_sds_pre(self, action):
        parameters = [self.get_basic_description(), action]
        prompt = generate_prompt(parameters, self.generate_sds_pre_template_path)
        content = json.loads(get_response(prompt))["choices"][0]["message"]["content"]
        sds = 2
        js_sds = content[content.find("{") : content.rfind("}") + 1]
        #reverse_num = ["2", "5", "6", "11", "12", "14", "16", "17", "18", "20"]

        ###
        flag=False
        for i in range(3):
            try:
                js_sds = json.loads(content[content.find("{") : content.rfind("}") + 1])
                flag=True
            except:
                print("重新生成sds")
                content = json.loads(get_response(prompt))["choices"][0]["message"]["content"]
            if(flag==True):
                break
            else:
                continue    
        if(flag):
            total = 0
            for key in js_sds.keys():
                score = js_sds[key]["score"]
                # if key in reverse_num:
                #     score = 5 - score
                total += score
            sds = total / 20
        else:
            print(f"sds_pre_debug:{content}")
            sds = 2
            print(
                f"修正失败，修正次数：3\n生成默认的sds:\n{sds}"
            )
            js_sds = {"默认初始sds值": 2}
        self.sds = sds
        sds_detail = json.dumps(js_sds, ensure_ascii=False)
        self.sds_detail = sds_detail
        ###
        return sds, sds_detail

    async def generate_sas_pre(self, action):
        parameters = [self.get_str_description(), action]
        prompt = generate_prompt(parameters, self.generate_sas_pre_template_path)
        content = json.loads(get_response(prompt))["choices"][0]["message"]["content"]
        sas = 50
        js_sas = content[content.find("{") : content.rfind("}") + 1]
        #reverse_num = ["5", "9", "13", "17", "19"]
###
        flag=False
        for i in range(3):
            try:
                js_sas = json.loads(content[content.find("{") : content.rfind("}") + 1])
                flag=True
            except:
                print("重新生成sas")
                content = json.loads(get_response(prompt))["choices"][0]["message"]["content"]
            if(flag==True):
                break
            else:
                continue    
        if(flag):
            total = 0
            for key in js_sas.keys():
                score = js_sas[key]["score"]
                # if key in reverse_num:
                #     score = 5 - score
                total += score
            sas = int(total * 1.25)
        else:
            print(f"sas_pre_debug:{content}")
            sas = 50
            print(
                f"修正失败，修正次数：3\n生成默认的sas:\n{sas}"
            )
            js_sas = {"默认初始sas值": sas}
        self.sas = sas
        sas_detail = json.dumps(js_sas, ensure_ascii=False)
        self.sas_detail = sas_detail

        return sas, sas_detail

    async def generate_mood_pre(self, action):
        """
        这个函数用于前测情绪，其实主要是拿一个action来测情绪，如果后面听取医生建议采取行动
        以后要看情绪反应也可以用这个函数。
        """
        parameters = [self.get_basic_description(), action]
        prompt = generate_prompt(parameters, self.generate_mood_prompt_pre_path)
        # print(f"生成的prompts：\n{prompt}")
        content = json.loads(get_response(prompt))["choices"][0]["message"]["content"]
        mood = ""
        try:
            js_mood = json.loads(content[content.find("{") : content.rfind("}") + 1])
            # print(f"生成的mood:\n{js_mood}")
            mood = js_mood["mood"]
        except:
            fix_result = fix_json_format_template(
                content[content.find("{") : content.rfind("}") + 1]
            )
            if fix_result["is_fix"] == "yes":
                mood = json.loads(fix_result["result"])["mood"]
                # print(f"修正mood成功，修正次数：{fix_result['num']}\n修正结果：{mood}")
            else:
                mood = self.mood  # 后续可以再做一个重问修正的步骤
                print("mood_pre_debug:", content)
                print(
                    f"修正mood失败，修正次数：{fix_result['num']}\n生成默认的mood（保持当前情绪）:{mood}"
                )

        self.mood = mood
        return mood

    def generate_action_detail(self, action_simple):
        """
        传入一个日程上写的event，生成这个event发生的细节
        """
        parameters = [
            self.get_str_description(),
            self.current_doctor_suggestion,
            self.today_actions,
            action_simple,
        ]
        prompt = generate_prompt(parameters, self.generate_action_detail_path)
        content = json.loads(get_response(prompt))["choices"][0]["message"]["content"]
        action_detail_js = {}
        action_detail = ""
        try:
            action_detail_js = json.loads(
                content[content.find("{") : content.rfind("}") + 1]
            )
            action_detail = content[content.find("{") : content.rfind("}") + 1]
        except:
            fix_result = fix_json_format_template(
                content[content.find("{") : content.rfind("}") + 1]
            )
            if fix_result["is_fix"] == "yes":
                action_detail = fix_result["result"]

            else:
                action_detail = action_simple  # 后续可以再做一个重问修正的步骤
                print("action_detail_debug:", content)
                print(
                    f"修正action_detail失败，修正次数：{fix_result['num']}\n保持当前输入进来的action_simple:{action_detail}"
                )
        return action_detail

    async def take_action(self, time_str):
        """
        给一个时间，如果这个时间对的上plan的起始时间的话就执行对应的行动(把日程上面记载的简单的event先变成包含细节的执行过程来执行)，
        并且得到实时心理情况反馈，并将这条记录添加到记忆中
        """
        record = {}
        mood = ""
        perma = 5
        perma_detail = ""

        sds = 0
        sds_detail = ""

        sas = 0
        sas_detail = ""
        
        gwb = 0
        gwb_detail = ""
        flag = False  # flag记录当前时间t有没有事件要执行
        for i, p in enumerate(self.plan):
            o_t = p["time"]
            # print(f"take_action:{o_t} {time_str}")
            if (
                p["time"] in time_str
            ):  # 传进来的time_str应该包含日期，plan里面的是不包含日期只有时间的
                flag = True
                simple_action = p["event"]
                action = self.generate_action_detail(
                    simple_action
                )  # 生成详细的event执行过程
                # print("action success")

                tasks=[asyncio.create_task(self.generate_mood_pre(action))
                    ,asyncio.create_task(self.generate_perma_pre(action))
                    ,asyncio.create_task(self.generate_sds_pre(action))
                    ,asyncio.create_task(self.generate_sas_pre(action))
                    ,asyncio.create_task(self.generate_gwb_pre(action))
                ]
                res_list = await asyncio.gather(*tasks)
                
                #提取结果
                mood = res_list[0]
                # print("mood success")
                self.mood = mood
                
                perma, perma_detail = res_list[1]
                self.perma = perma
                self.perma_detail = perma_detail
                
                sds, sds_detail = res_list[2]
                self.sds = sds
                self.sds_detail = sds_detail

                sas, sas_detail = res_list[3]
                self.sas = sas
                self.sas_detail = sas_detail

                gwb, gwb_detail = res_list[4]
                self.gwb = gwb
                self.gwb_detail = gwb_detail

                record = {
                    "time": time_str,
                    "action": action,
                    "mood": self.mood,
                    "perma": self.perma,
                    "sds": self.sds,
                    "sas": self.sas,
                    "gwb": self.gwb
                }
                self.action = record
                # print(f"活动记录：{record}")
                # 加到memory里面
                self.add_recent_actions(record)
                # print("add recent action success")
                self.add_today_actions(record)
                # print("add today action success")
                self.daily_memory.add(
                    [
                        Document(
                            page_content=str(record),
                            metadata={"source": "daily_record", "timestamp": time_str},
                        )
                    ]
                )
                # print("update memory action success")
                break
            else:
                continue
        return record, mood, perma, perma_detail, sds, sds_detail, sas, sas_detail, gwb, gwb_detail, flag

    # def generate_perma_after_intervention(self,intervention_record):
    def generate_resident_reply(self, question):
        """
        用于生成医生提的问题的回答
        question传进来应该是一个这样的结构：
        [
            {
                "1": "小李，你在忙碌的工作之余，有没有什么特别的方式来奖励自己，提高工作的积极性呢？"
            },
            {
                "2": "与小刚和小红的互动对你来说似乎很重要，你们在一起时有什么特别的乐趣或者能让你放松的活动吗？试着多分享这些时刻，它们对你的心理健康很有帮助。"
            }
        ]
        """
        description = self.get_str_description()
        related_daily_memory = []
        related_medical_memory = []
        for item in question:
            rdm = ""
            rmm = ""
            for key in item.keys():
                rdm += str(self.daily_memory.query(item[key])["documents"])
                rmm += str(self.medical_memory.query(item[key])["documents"])
            related_daily_memory.append(rdm)
            related_medical_memory.append(rmm)
        parameters = [
            description,
            self.action,
            question,
            str(related_daily_memory) + "\n" + str(related_medical_memory),
        ]
        prompt = generate_prompt(parameters, self.generate_resident_reply_path)
        # print(f"生成的prompts：\n{prompt}")
        completion = get_response(prompt)
        content = json.loads(completion)["choices"][0]["message"]["content"]
        reply = content[content.find("[") : content.rfind("]") + 1]
        # print(f"回复：{reply}")
        return reply

    def accept_or_not(self, suggestion):
        """
        生成居民是否接受医生建议的决定以及背后的原因，同时修改self.current_doctor_suggestion，记录最近doctor对该居民agent的建议
        """
        description = self.get_str_description()
        related_medical_memory = self.medical_memory.query(
            f"当前行为与感受：{self.action}\n当前医生的建议：{suggestion}\n对心理干预的偏好:{self.preference_on_suggestions}"
        )
        parameters = [
            description,
            self.plan,
            self.action,
            self.preference_on_suggestions,
            related_medical_memory,
            suggestion,
        ]
        prompt = generate_prompt(parameters, self.accept_or_not_path)
        # print(f"生成的prompts：\n{prompt}")
        completion = get_response(prompt)
        content = json.loads(completion)["choices"][0]["message"]["content"]
        accept = ""
        try:
            accept = json.loads(content[content.find("{") : content.rfind("}") + 1])
            if accept["choice"] == "no":
                self.current_doctor_suggestion = "暂无"
            else:
                self.current_doctor_suggestion = suggestion
            # print(f"生成的choice：{accept}")
        except:
            fix_result = fix_json_format_template(
                content[content.find("{") : content.rfind("}") + 1]
            )
            if fix_result["is_fix"] == "yes":
                accept = json.loads(fix_result["result"])
                self.current_doctor_suggestion = suggestion
                # print(f"修正accept_or_not成功，修正次数：{fix_result['num']}\n修正结果：{accept}")
            else:
                accept = {
                    "choice": "no",
                    "reason": "我不喜欢他的建议，我觉得他的建议难以实现，而且不适合我的情况",
                }
                print("mood_pre_debug:", content)
                self.current_doctor_suggestion = "暂无"
                print(
                    f"修正accept_or_not失败，修正次数：{fix_result['num']}\n生成默认的accept状态（no）:{accept}"
                )
        return accept

    async def generate_perma_with_dialogue(
        self, question, reply, suggestion, accept, perma_pre_detail, inplace=True
    ):
        """
        在病人决定不采纳医生建议的时候会用到的，用医疗过程以及前测perma来预测后测perma
        """
        parameters = [
            self.get_basic_description(),
            question,
            reply,
            suggestion,
            accept,
            perma_pre_detail,
        ]
        prompt = generate_prompt(parameters, self.generate_perma_with_dialogue_path)
        # print(f"生成的prompts：\n{prompt}")
        content = json.loads(get_response(prompt))["choices"][0]["message"]["content"]
        perma = 0
        js_perma = ""
        try:
            js_perma = json.loads(content[content.find("{") : content.rfind("}") + 1])
            # print(f"生成的perma:\n{js_perma}")
            total = 0
            for key in js_perma.keys():
                total += js_perma[key]["score"]
            perma = total / 23
        except:
            # print(f"perma_debug:{content}")
            perma = 5  # 后续可以再做一个重问修正的步骤
            # print(f"生成默认的perma:\n{perma}")
            js_perma = {"默认初始perma值": 5}
        perma_detail = json.dumps(js_perma, ensure_ascii=False)
        if inplace:
            self.perma = perma
            self.perma_detail = perma_detail
        return perma, perma_detail

    async def generate_sds_with_dialogue(
        self, question, reply, suggestion, accept, sds_pre_detail, inplace=True
    ):
        """
        在病人决定不采纳医生建议的时候会用到的，用医疗过程以及前测sds来预测后测sds
        """
        parameters = [
            self.get_basic_description(),
            question,
            reply,
            suggestion,
            accept,
            sds_pre_detail,
        ]
        prompt = generate_prompt(parameters, self.generate_sds_with_dialogue_path)
        # print(f"生成的prompts：\n{prompt}")
        content = json.loads(get_response(prompt))["choices"][0]["message"]["content"]
        sds = 2
        #reverse_num = [2, 5, 6, 11, 12, 14, 16, 17, 18, 20]
        flag = False
        for _ in range(3):
            try:
                js_sds = json.loads(content[content.find("{") : content.rfind("}") + 1])
                flag = True
                break
            except:
                print("重新生成sds")
                content = json.loads(get_response(prompt))["choices"][0]["message"][
                    "content"
                ]
        if flag:
            total = 0
            for key in js_sds.keys():
                score = js_sds[key]["score"]
                # if key in reverse_num:
                #     score = 5 - score
                total += score
            sds = total / 20
        else:
            print(f"sds_pre_debug:{js_sds}")
            js_sds = {"默认初始sds值": sds}

        sds_detail = json.dumps(js_sds, ensure_ascii=False)
        if inplace:
            self.sds = sds
            self.sds_detail = json.dumps(js_sds, ensure_ascii=False)
        return sds, sds_detail

    async def generate_sas_with_dialogue(
        self, question, reply, suggestion, accept, sas_pre_detail, inplace=True
    ):
        """
        用医疗过程以及前测sas来预测后测sas
        """
        parameters = [
            self.get_basic_description(),
            question,
            reply,
            suggestion,
            accept,
            sas_pre_detail,
        ]
        prompt = generate_prompt(parameters, self.generate_sas_with_dialogue_path)
        content = json.loads(get_response(prompt))["choices"][0]["message"]["content"]
        sas = 2
        #reverse_num = [5, 9, 13, 17, 19]
        flag = False
        for _ in range(3):
            try:
                js_sas = json.loads(content[content.find("{") : content.rfind("}") + 1])
                flag = True
                break
            except:
                print("重新生成sas")
                content = json.loads(get_response(prompt))["choices"][0]["message"][
                    "content"
                ]
        if flag:
            total = 0
            for key in js_sas.keys():
                score = js_sas[key]["score"]
                # if key in reverse_num:
                #     score = 5 - score
                total += score
            sas = int(total * 1.25)
        else:
            print(f"sas_pre_debug:{js_sas}")
            js_sas = {"默认初始sas值": sas}

        sas_detail = json.dumps(js_sas, ensure_ascii=False)
        if inplace:
            self.sas = sas
            self.sas_detail = json.dumps(js_sas, ensure_ascii=False)
        return sas, sas_detail

    async def generate_gwb_with_dialogue(
        self, question, reply, suggestion, accept, gwb_pre_detail, inplace=True
    ):
        """
        用医疗过程以及前测perma来预测后测perma
        """
        parameters = [
            self.get_basic_description(),
            question,
            reply,
            suggestion,
            accept,
            gwb_pre_detail,
        ]
        prompt = generate_prompt(parameters, self.generate_gwb_with_dialogue_path)
        # print(f"生成的prompts：\n{prompt}")
        content = json.loads(get_response(prompt))["choices"][0]["message"]["content"]
        gwb = 0
        js_gwb = ""
        flag=False
        for i in range(3):
            try:
                js_gwb = json.loads(content[content.find("{") : content.rfind("}") + 1])
                flag=True
            except:
                print("重新生成gwb_dialogue")
                content = json.loads(get_response(prompt))["choices"][0]["message"]["content"]
            if(flag):
                
                break
            else:
                continue  
        if(flag):
            total = 0
            for key in js_gwb.keys():
                total += js_gwb[key]["score"]
            gwb = total
        else:
            gwb = 75  # 后续可以再做一个重问修正的步骤
            js_gwb = {"默认初始perma值": 75}
        gwb_detail = json.dumps(js_gwb, ensure_ascii=False)
        if inplace:
            self.gwb = gwb
            self.gwb_detail = gwb_detail
        return gwb, gwb_detail

    def generate_mood_with_dialogue(
        self,
        question,
        reply,
        suggestion,
        accept,
        perma_pre_simple,
        mood_pre,
        perma_post_simple,
        inplace=True,
    ):
        """
        当病人拒绝采用医生建议的时候用这个函数得到他的情绪状态
        这里传入的perma，全部只需要一个值就可以了
        """
        parameters = [
            self.get_basic_description(),
            question,
            reply,
            suggestion,
            accept,
            perma_pre_simple,
            mood_pre,
            perma_post_simple,
        ]
        prompt = generate_prompt(parameters, self.generate_mood_with_dialogue_path)
        # print(f"生成的prompts：\n{prompt}")
        content = json.loads(get_response(prompt))["choices"][0]["message"]["content"]
        mood = ""
        try:
            mood = json.loads(content[content.find("{") : content.rfind("}") + 1])[
                "mood"
            ]
            # print(f"生成的mood（dialogue）：{mood}")
        except:
            result = fix_json_format_template(content)
            if result["is_fix"] == True:
                mood = json.loads(result["result"])["mood"]
                # print(f"修正mood（dialogue）成功：\n修正次数：{result['num']}\n结果：{mood}")
            else:
                print(
                    f"修正mood（dialogue）失败，修正次数：{result['num']}\n debug：{content}\n保持原来的mood:{self.mood}"
                )
                mood = self.mood
        if inplace:
            self.mood = mood
        return mood

    def update_memory(
        self,
        time_str,
        question,
        reply,
        suggestion,
        accept,
        perma_pre_simple,
        mood_pre,
        perma_post_simple,
        mood_post,
    ):
        """
        更新病人agent的memory
        """
        parameters = [
            time_str,
            question,
            reply,
            suggestion,
            accept,
            perma_pre_simple,
            mood_pre,
            perma_post_simple,
            mood_post,
        ]
        memory_text = generate_prompt(parameters, self.update_memory_path)
        # print(f"居民agent增加的干预记忆：\n{memory_text}")
        memory_d = [
            Document(
                page_content=memory_text,
                metadata={"source": "medical_record", "timestamp": time_str},
            )
        ]
        self.medical_memory.add(memory_d)

    def change_plan(self, time_str):
        parameters = [
            self.get_str_description(),
            self.daily_requirement,
            self.plan,
            self.current_doctor_suggestion,
            time_str,
        ]
        prompt = generate_prompt(parameters, self.change_plan_path)

        content = json.loads(get_response(prompt))["choices"][0]["message"]["content"]
        js_plan = 0
        # js_plan=json.loads(rs[rs.find("{"):rs.rfind("}")+1])
        try:
            js_plan = json.loads(content[content.find("[") : content.rfind("]") + 1])
            # print(f"生成的plan:\n{js_plan}")
        except:
            fix_result = fix_json_format_template(
                content[content.find("[") : content.rfind("]") + 1]
            )
            if fix_result["is_fix"] == "yes":
                # print(f"修正的plan:\n修正次数{fix_result['num']}\n修正结果：{fix_result['result']}")
                js_plan = fix_result["result"]
            else:
                if self.plan != 0:
                    js_plan = (
                        self.plan
                    )  # 生成失败让他直接执行上前天的计划，后续写完memory把这里改成重复提问让agent修正的做法
                    print(f"debug_change_plan:\n{content}")
                    print(
                        f"修正失败:\n修正次数{fix_result['num']}\n延续前一天计划：{js_plan}"
                    )
                else:
                    js_plan = self.default_plan
                    print(f"debug_change_plan:\n{content}")
                    print(
                        f"修正失败:\n修正次数{fix_result['num']}\n采用默认计划：{js_plan}"
                    )
        self.plan = js_plan
        return js_plan

    def resident_help_with_law(self, perma_now):
        """
        居民是否需要心理医生的帮助，根据一个perma_law值，perma小于这个值直接需要帮助
        返回一个json格式的东西，例如：
        {"choice":"yes",reason:"我心情很差，需要寻求心理医生帮助"}
        """
        perma_law = self.perma_law
        rs = {}
        if perma_now < perma_law:
            rs = {
                "choice": "yes",
                "reason": f"当前比平时的情绪状态差(perma值低于{self.name}日常perma正常值{self.perma_law})，需要寻求心理医生的帮助。",
            }
        else:
            rs = {
                "choice": "no",
                "reason": f"当前情绪状态正常(perma值高于{self.name}日常perma正常{self.perma_law})，不需要寻求心理医生的帮助。",
            }

        print(f"help_with_law:\nperma_now:{perma_now}\nperma_law:{perma_law}\nrs:{rs}\n")
        return rs

    def resident_help_with_llm(self):
        """
        居民是否需要心理医生的帮助
        返回一个json格式的东西，例如：
        {"choice":"yes",reason:"我心情很差，需要寻求心理医生帮助"}
        """
        parameters = [self.get_basic_description(), self.action]
        prompt = generate_prompt(parameters, self.resident_help_path)
        # print(f"resident_help_promt:\n{prompt}")
        content = json.loads(get_response(prompt))["choices"][0]["message"]["content"]
        accept = {}
        try:
            accept = json.loads(content[content.find("{") : content.rfind("}") + 1])
            # print(f"生成的choice：{accept}")
        except:
            fix_result = fix_json_format_template(
                content[content.find("{") : content.rfind("}") + 1]
            )
            if fix_result["is_fix"] == "yes":
                accept = json.loads(fix_result["result"])
                # print(f"修正accept_or_not成功，修正次数：{fix_result['num']}\n修正结果：{accept}")
            else:
                accept = {"choice": "no", "reason": "我还不需要心理医生的帮助。"}
                print("resident_help_debug:", content)
                print(
                    f"修正resident_help失败，修正次数：{fix_result['num']}\n生成默认的accept状态（no）:{accept}"
                )
        return accept

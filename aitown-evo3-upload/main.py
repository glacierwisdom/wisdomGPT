import argparse
from llm import *
from resident_agent import ResidentAgent
from doctor_agent import DoctorAgent
from memory1 import Memory
from global_method import *
import json
from langchain_core.documents import Document
from mysql_operation import *
from god import GodAgent
import asyncio
from init_utils import *
def add_record(path, text):
    with open(path, "a") as f:
        current_time = datetime.now()
        time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"记录生成时间：{time_str}\n{text}")

async def single_doctor_resident_interact(agent, doctor, i, is_help, perma_detail_pre, perma_pre, mood_pre, sds_detail_pre, sas_detail_pre, gwb_detail_pre):
    rs={}
    print(f"医生<{doctor.name}>生成问题")
    question = json.loads(doctor.generate_doctor_question(agent))
    rs["question"]=question
    
    print(f"病人回复<{doctor.name}>")
    reply = agent.generate_resident_reply(question)
    rs["reply"]=reply

    print(f"医生<{doctor.name}>生成病人画像")
    portrait = doctor.generate_resident_portrait(
        agent, agent.recent_actions, is_help, question, reply
    )
    rs["portrait"]=portrait
    

    print(f"医生<{doctor.name}>生成建议")
    suggestion = doctor.generate_doctor_suggestion(
        agent, question, reply
    )
    rs["doctor_suggestion"]=suggestion

    print(f"基于医生<{doctor.name}>的建议，居民开始进行后测")
    tasks=[asyncio.create_task(agent.generate_perma_with_dialogue(question,reply,suggestion,"未知",perma_detail_pre,inplace=False)),
           asyncio.create_task(agent.generate_sds_with_dialogue(question,reply,suggestion,"未知",sds_detail_pre,inplace=False)),
            asyncio.create_task(agent.generate_sas_with_dialogue(question,reply,suggestion,"未知",sas_detail_pre,inplace=False)),
            asyncio.create_task(agent.generate_gwb_with_dialogue(question,reply,suggestion,"未知",gwb_detail_pre,inplace=False)),
            ]
    res_list=await asyncio.gather(*tasks)
    perma_dialogue, perma_dialogue_detail = res_list[0]
    sds_dialogue, sds_dialogue_detail = res_list[1]
    sas_dialogue, sas_dialogue_detail = res_list[2]
    gwb_dialogue, gwb_dialogue_detail = res_list[3]

    mood_dialogue = agent.generate_mood_with_dialogue(question,reply,suggestion,"未知",perma_pre, mood_pre, perma_dialogue,inplace=False)               
    print(f"基于医生<{doctor.name}>的建议，居民后测结束")       
    rs["perma_dialogue"]=perma_dialogue
    rs["perma_dialogue_detail"]=perma_dialogue_detail
    rs["sds_dialogue"]=sds_dialogue
    rs["sds_dialogue_detail"]=sds_dialogue_detail
    rs["sas_dialogue"]=sas_dialogue
    rs["sas_dialogue_detail"]=sas_dialogue_detail
    rs["gwb_dialogue"]=gwb_dialogue
    rs["gwb_dialogue_detail"]=gwb_dialogue_detail
    rs["mood_dialogue"] = mood_dialogue
    ###
    return rs
    
async def run(
    record_path,
    reference_num,
    agent,
    doctor_list,
    god,
    args,
    days=2,
    forget_day=1,
    start_time_str="2024-7-24 00:00:00",
    interval_seconds=3600,
):
    t = ""
    sts = start_time_str
    interval_seconds = 3600
    for d in range(days):
        agent.reset_today_actions()  # 重置今日action记录
        print(f"-------------------\n第{d}天开始：")
        if((d+1)%forget_day==0):
            agent.current_doctor_suggestion = "无"  # 达到指定forget_day后重置resident的医生建议，避免一个建议一直生效，这样不符合客观规律，这里可以写个跟天数相关的概率函数优化。
        
        #agent.current_doctor_suggestion = "无"  # 重置resident的医生建议，避免一个建议一直生效，这样不符合客观规律，这里可以写个跟天数相关的概率函数优化。
        time_series = generate_time_series(sts, interval_seconds)
        print("生成日程")
        plan = agent.generate_plan(0, 0)
        add_record(
            record_path,
            f"\n----------------------------------------------------\n第{d}天的日程：\n{plan}\n\n",
        )
        for t in time_series:
            print(f"时间：{t}")
            print("执行action")
            record, mood_pre, perma_pre, perma_detail_pre, sds_pre, sds_detail_pre, sas_pre, sas_detail_pre, gwb_pre, gwb_detail_pre, flag = await agent.take_action(t)
            if flag:
                # print(f"{t}时刻执行的动作：{record}")
                
                add_record(record_path, f"第{d}天{t}时刻执行的动作：{record}\n\n")

                is_help = agent.resident_help_with_law(perma_pre)
                print(f"判断居民是否需要心理医生帮助{perma_pre}\n{is_help}")
                add_record(record_path, f"第{d}天{t}时刻是否需要心理医生帮助：{is_help}\n\n")
                current_time = datetime.now()
                time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')
                daily_record_id = insert_resident_daily_record(
                    args.experiment,
                    d,
                    t,
                    record["action"],
                    perma_pre,
                    perma_detail_pre,
                    sds_pre,
                    sds_detail_pre,
                    sas_pre,
                    sas_detail_pre,
                    gwb_pre,
                    gwb_detail_pre,
                    mood_pre,
                    -1,
                    is_help["choice"],
                    is_help["reason"],
                    agent.name,
                    time_str,
                )

                if is_help["choice"] == "yes":
                    # 需要医生帮忙的时候
                    print("居民需要医生帮忙")
                    questions = ""
                    replies = ""
                    doctor_portraits = ""
                    doctor_suggestions = ""  # 用于生成god建议的时候用
                    doctor_suggestion_list = []  # 用于看完病以后更新记忆的时候用
                    perma_dialogue_all = []
                    perma_dialogue_detail_all = []
                    sds_dialogue_all = []
                    sds_dialogue_detail_all = []
                    sas_dialogue_all = []
                    sas_dialogue_detail_all = []
                    gwb_dialogue_all = []
                    gwb_dialogue_detail_all = []
                    mood_dialogue_all = []
                    question_list = []
                    reply_list = []
                    tasks= []
                    add_record(record_path, f"第{d}天{t}时刻各个心理医生开始进行心理干预\n\n")
                    for j, doctor in enumerate(doctor_list):
                        tasks.append(asyncio.create_task(single_doctor_resident_interact(agent, doctor, j, is_help, perma_detail_pre, perma_pre, mood_pre,  sds_detail_pre, sas_detail_pre, gwb_detail_pre)))
                    res_list = await asyncio.gather(*tasks)
                    for m, rs in enumerate(res_list):
                        
                        doctor=doctor_list[m]
                        question = rs["question"]
                        questions = questions + f"{question}\n"   
                        question_list.append(question)
                        add_record(record_path, f"第{d}天{t}时刻医生<{doctor.name}>生成的问题：{question}\n")

                        reply = rs["reply"]
                        replies = replies + f"{reply}\n"   
                        reply_list.append(reply)
                        add_record(record_path, f"第{d}天{t}时刻病人生成对医生<{doctor.name}>的回答：{reply}\n")

                        portrait = rs["portrait"]
                        doctor_portraits = doctor_portraits + f"{doctor.name}对该病人的画像:\n该医生擅长的领域:{doctor.style}\n该医生生成的画像:{portrait}\n\n"
                        add_record(record_path, f"第{d}天{t}时刻医生<{doctor.name}>生成的病人画像：{portrait}\n")
                        
                        suggestion = rs["doctor_suggestion"]
                        doctor_suggestion_list.append(suggestion)
                        doctor_suggestions = doctor_suggestions + f"{doctor.name}提的建议:\n该医生擅长的领域:{doctor.style}\n该医生提的建议:{suggestion}\n\n"
                        add_record(record_path, f"第{d}天{t}时刻医生<{doctor.name}>生成的建议：{suggestion}\n")

                        perma_dialogue = rs["perma_dialogue"]
                        perma_dialogue_detail = rs["perma_dialogue_detail"]
                        mood_dialogue = rs["mood_dialogue"]
                        perma_dialogue_all.append(float(perma_dialogue))
                        perma_dialogue_detail_all.append(perma_dialogue_detail)
                        mood_dialogue_all.append(mood_dialogue)
                        sds_dialogue = rs["sds_dialogue"]
                        sds_dialogue_detail = rs["sds_dialogue_detail"]
                        sds_dialogue_all.append(float(sds_dialogue))
                        sds_dialogue_detail_all.append(sds_dialogue_detail)
                        sas_dialogue = rs["sas_dialogue"]
                        sas_dialogue_detail = rs["sas_dialogue_detail"]
                        sas_dialogue_all.append(float(sas_dialogue))
                        sas_dialogue_detail_all.append(sas_dialogue_detail)
                        gwb_dialogue = rs["gwb_dialogue"]
                        gwb_dialogue_detail = rs["gwb_dialogue_detail"]
                        gwb_dialogue_all.append(float(gwb_dialogue))
                        gwb_dialogue_detail_all.append(gwb_dialogue_detail)
                        add_record(record_path, f"第{d}天{t}时刻假如接受{doctor.name}的心理干预后病人情况：\n情绪：{mood_dialogue}\nperma值：{perma_dialogue}\nsds:{sds_dialogue}\nsas:{sas_dialogue}\ngwb:{gwb_dialogue}\n\n")

                    
                    print("god生成病人画像")
                    god_portrait = god.generate_portrait_god(
                        agent,
                        agent.recent_actions,
                        is_help,
                        questions,
                        replies,
                        doctor_portraits,
                    )
                    
                    add_record(
                        record_path, f"第{d}{t}时刻god生成的病人画像：{god_portrait}\n"
                    )

                    print("god生成建议")
                    god_suggestion = god.generate_god_suggestion(
                        agent, doctor_suggestions, reference_num
                    )
                    print("god_suggestion:", god_suggestion)
                    current_time = datetime.now()
                    time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')
                    add_record(
                        record_path, f"第{d}{t}时刻god生成的病人画像：{god_portrait}\n"
                    )

                    print("病人判断是否接god建议")
                    accept = agent.accept_or_not(god_suggestion)
                    # print(f"{t}时刻病人对医生建议的反馈：{accept}")
                    
                    add_record(record_path, f"第{d}天{t}时刻病人对上帝建议的反馈：{accept}\n")
                    # print(f"perma_detail_pre:{perma_detail_pre}")
                    ###todo
                    print("病人对god意见进行后测")
                    add_record(record_path, f"第{d}天{t}时刻病人对上帝的建议开始进行反馈（后测）\n")
                    tasks=[
                    asyncio.create_task(agent.generate_perma_with_dialogue("", "", god_suggestion, accept, perma_detail_pre))
                    ,asyncio.create_task(agent.generate_sds_with_dialogue("", "", god_suggestion, accept, sds_detail_pre))
                    ,asyncio.create_task(agent.generate_sas_with_dialogue("", "", god_suggestion, accept, sas_detail_pre))
                    ,asyncio.create_task(agent.generate_gwb_with_dialogue("", "", god_suggestion, accept, gwb_detail_pre))
                    ]
                    res_list = await asyncio.gather(*tasks)
                    perma_dialogue_god, perma_dialogue_detail_god=res_list[0]
                    sds_dialogue_god, sds_dialogue_detail_god=res_list[1]
                    sas_dialogue_god, sas_dialogue_detail_god=res_list[2]
                    gwb_dialogue_god, gwb_dialogue_detail_god=res_list[3]
                    mood_dialogue_god = agent.generate_mood_with_dialogue(
                        "",
                        "",
                        god_suggestion,
                        accept,
                        perma_pre,
                        mood_pre,
                        perma_dialogue_god,
                    )
                    ####
                    # print(f"{t}时刻心理干预后病人情况：\nperma值：{perma_dialogue}\n情绪：{mood_dialogue_god}")
                    add_record(
                        record_path,
                        f"第{d}天{t}时刻接受god的心理干预后病人情况：\nperma值：{perma_dialogue_god}\n情绪：{mood_dialogue_god}\nsds值：{sds_dialogue_god}\nsas值：{sas_dialogue_god}\ngwb值：{gwb_dialogue_god}\n\n",
                    )

                    # 以下是判断god的建议好不好的部分
                    max_doctor_perma_dialogue = max(perma_dialogue_all)
                    accept_doctor_list = (
                        []
                    )  # 储存在下面的规则下，最终每个医生的建议是好还是坏

                    if accept["choice"] == "no":  # 居民不接受该建议时
                        for k in range(len(doctor_list)):
                            if god_suggestion["reference"][k]["fit"] == "yes":
                                accept_doctor_list.append(accept)
                            else:
                                accept_doctor_list.append(
                                    {
                                        "choice": "no",
                                        "reason": god_suggestion["reference"][k]["reason"],
                                    }
                                )
                    elif (max_doctor_perma_dialogue >= perma_dialogue_god):  # 居民接受该建议，但god的建议不是最佳建议
                        better_suggestion = ""
                        for k in range(len(perma_dialogue_all)):
                            if perma_dialogue_all[k] >= perma_dialogue_god:
                                accept_doctor_list.append(
                                    {
                                        "choice": "yes",
                                        "reason": doctor_suggestion_list[k]["reason"],
                                    }
                                )
                                better_suggestion += (
                                    f"{k}：{doctor_suggestion_list[k]['suggestion']}\n"
                                )
                            else:
                                accept_doctor_list.append(
                                    {
                                        "choice": god_suggestion["reference"][k]["fit"],
                                        "reason": god_suggestion["reference"][k][
                                            "reason"
                                        ],
                                    }
                                )
                        accept = {
                            "choice": "yes_but_not_the_best",
                            "reason": f"不如以下建议：{better_suggestion}",
                        }
                        # agent.current_doctor_suggestion=better_suggestion
                    else:  # 居民接受建议，同时god的建议是最佳建议
                        for k in range(len(perma_dialogue_all)):
                            sug = god_suggestion["reference"][k]
                            choice = sug["fit"] if "fit" in sug.keys() else ""
                            reason = sug["reason"] if "reason" in sug.keys() else ""
                            accept_doctor_list.append(
                                {"choice": choice, "reason": reason}
                            )

                    add_record(
                        record_path,
                        f"第{d}天{t}时刻经过规则干预后，病人对上帝建议的最终反馈：{accept}\n\n",
                    )

                    # 更新居民向量数据库的记忆
                    agent.update_memory(
                        t,
                        questions,
                        replies,
                        god_suggestion["suggestion"]["suggestion_content"],
                        accept,
                        perma_pre,
                        mood_pre,
                        perma_dialogue_god,
                        mood_dialogue_god,
                    )

                    # 记录god的medical记录，medical记录的daily_record_id是发出请求帮助的action（即执行完这个action就转到心理干预环节）
                    god_medical_id = insert_medical_record(
                        record_path,
                        daily_record_id,
                        "",
                        "",
                        god_suggestion["suggestion"]["suggestion_content"],
                        god_suggestion["suggestion"]["reason"],
                        perma_pre,
                        perma_dialogue_god,
                        perma_dialogue_detail_god,
                        mood_pre,
                        mood_dialogue_god,
                        accept["choice"],
                        accept["reason"],
                        agent.name,
                    )

                    # 这里插入一个“接受心理干预”的action是为了方便统计绘图，他的medical_id指向这次干预记录详细情况
                    current_time = datetime.now()
                    time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')
                
                    insert_resident_daily_record(
                        args.experiment,
                        d,
                        t,
                        "接受心理干预",
                        perma_dialogue_god,
                        perma_dialogue_detail_god,
                        sds_dialogue_god,
                        sds_dialogue_detail_god,
                        sas_dialogue_god,
                        sas_dialogue_detail_god,
                        gwb_dialogue_god,
                        gwb_dialogue_detail_god,
                        mood_dialogue_god,
                        god_medical_id,
                        is_help["choice"],
                        is_help["reason"],
                        agent.name,
                        time_str
                    )

                    # doctor的medical记录，以及god和doctor的medical记录之间的关联
                    for l, doctor in enumerate(doctor_list):
                        doctor_medical_id = insert_medical_record(
                            record_path,
                            daily_record_id,
                            question_list[l],
                            reply_list[l],
                            doctor_suggestion_list[l]["suggestion"],
                            doctor_suggestion_list[l]["reason"],
                            perma_pre,
                            perma_dialogue_all[l],
                            perma_dialogue_detail_all[l],
                            mood_pre,
                            mood_dialogue_all[l],
                            accept_doctor_list[l]["choice"],
                            accept_doctor_list[l]["reason"],
                            agent.name,
                        )
                        god_doctor_connection_id = insert_god_doctor_connection(
                            doctor_medical_id,
                            record_path,
                            god_medical_id,
                            god_suggestion["reference"][l]["fit"],
                            god_suggestion["reference"][l]["reason"],
                            accept_doctor_list[l]["choice"],
                            accept_doctor_list[l]["reason"],
                            d,
                            t,
                        )
                        doctor.update_memory(
                            t,
                            agent,
                            question_list[l],
                            reply_list[l],
                            doctor_suggestion_list[l],
                            accept_doctor_list[l],
                            perma_pre,
                            mood_pre,
                            perma_dialogue_all[l],
                            mood_dialogue_all[l],
                        )
                    god.update_memory(
                        t,
                        agent,
                        doctor_suggestion_list,
                        god_suggestion["reference"],
                        god_suggestion["suggestion"],
                        accept,
                        perma_pre,
                        mood_pre,
                        perma_dialogue_god,
                        mood_dialogue_god,
                    )

                    if (
                        accept["choice"] == "yes"
                    ):  # 如果病人接受医生建议，那么就重新规划当天当前时间点以后的日程
                        change_plan_start_time = t.strip().split(" ")[
                            -1
                        ]  # t的格式是%Y-%m-%d %H:%M:%S，处理后得到change_plan_start_time是一个%H:%M:%S的时间string
                        print("接受医生建议，重新规划日程")
                        plan = agent.change_plan(change_plan_start_time)
                        # print(f"第{d}天，时刻{t}新生成的日程：\n{plan}")
                        add_record(
                            record_path, f"第{d}天，时刻{t}新生成的日程：\n{plan}\n\n"
                        )
                else:
                    # 不需要帮忙的时候
                    print("不需要帮忙，继续执行之后的日程。")
            else:
                # 日程上当前时间t没有动作执行的时候
                # print(f"take no action {t}")
                print("当前时间点无动作需要执行")
        sts = t  # 更新sts，用于下一天生成时间序列

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--experiment', help='实验名字', default='test_default')
    parser.add_argument('-d', '--days', type=int, help='实验天数', default=2)
    parser.add_argument('-rmp', '--resident_mean_perma', type=float, help='居民日常perma的均值', default=5)
    parser.add_argument('-rsp', '--resident_std_perma', type=float, help='居民日常perma的标准差', default=0.5)
    parser.add_argument('-sl', '--resident_std_law', type=float, help='perma低于多少个标准差要去看医生', default=1)
    parser.add_argument('-fd', '--forget_day', type=int, help='多少天重置医生建议', default=1)
    parser.add_argument('-ri', '--resident_id', type=int, help='居民id', default=1)
    args = parser.parse_args()

    #初始化一个居民agent和四个医生agent以及一个god agent
    
    
    perma_mean=args.resident_mean_perma
    perma_std=args.resident_std_perma
    perma_law=perma_mean-perma_std*args.resident_std_law
    agent = init_agent(args.experiment, args.resident_id, perma_mean, perma_std, perma_law)
    doctor1 = init_doctor(args.experiment, 2)
    doctor2 = init_doctor(args.experiment, 3)
    doctor3 = init_doctor(args.experiment, 4)
    doctor4 = init_doctor(args.experiment, 6)

    doctor_list=[doctor1, doctor2, doctor3, doctor4]
    #doctor_list=[doctor1, doctor2]
    prompt_template="./prompt_template"
    memory_path=f"./chromadb/{args.experiment}/god/"
    god=GodAgent(prompt_template, memory_path)
    record_path=f"./record/{args.experiment}.txt"
    asyncio.get_event_loop()
    asyncio.run(run(record_path=record_path, agent=agent, doctor_list=doctor_list, args=args, god=god, 
                    days=args.days, reference_num=2,forget_day=args.forget_day))
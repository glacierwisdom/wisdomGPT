from llm import *
from memory1 import Memory
from global_method import *
import json
from resident_agent import ResidentAgent
from doctor_agent import DoctorAgent
from langchain_core.documents import Document
from mysql_operation import *
from god import GodAgent
import statistics
import argparse
import asyncio
from datetime import datetime
from init_utils import *
def add_record(path, text):
    with open(path, "a") as f:
        f.write(text)

    
async def test_init_perma(record_path, agent, args, days=2,
    start_time_str="2024-7-24 00:00:00",
    interval_seconds=3600):
    t = ""
    sts = start_time_str
    interval_seconds = 3600
    perma_list=[]
    sds_list=[]
    sas_list=[]
    gwb_list=[]
    for d in range(days):
        agent.reset_today_actions()  # 重置今日action记录
        print(f"-------------------\n第{d}天开始：")
        agent.current_doctor_suggestion = "无"  # 重置resident的医生建议，避免一个建议一直生效，这样不符合客观规律，这里可以写个跟天数相关的概率函数优化。
        time_series = generate_time_series(sts, interval_seconds)
        #print("time_series:",time_series)
        print("生成日程")
        plan = agent.generate_plan(0, 0)
        print(plan)
        current_time = datetime.now()
        time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')
        add_record(record_path, f"record_create_time:{time_str}\n第{d}天生成日程：\n{plan}\n\n")
        for t in time_series:
            print(f"时间：{t}")
            print("执行action")
            record, mood, perma, perma_detail, sds, sds_detail, sas, sas_detail, gwb, gwb_detail, flag = await agent.take_action(t)
            if flag:
                perma_list.append(record["perma"])
                sds_list.append(record["sds"])
                sas_list.append(record["sas"])
                gwb_list.append(record["gwb"])
                print(record)
                current_time = datetime.now()
                time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')
                add_record(record_path, f"record_create_time:{time_str}\n第{d}天，时间{t}执行动作，动作结果：\n{record}\n\n")
                insert_resident_daily_record(args.experiment,
                    d,
                    t,
                    record["action"],
                    perma,
                    perma_detail,
                    sds,
                    sds_detail,
                    sas,
                    sas_detail,
                    gwb,
                    gwb_detail,
                    mood,
                    -1,
                    "init_test",
                    "init_test",
                    agent.name,
                    time_str)
            else:
                print("当前时间点无动作需要执行")
                current_time = datetime.now()
                time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')
                add_record(record_path, f"record_create_time:{time_str}\n第{d}天，时间{t}无动作执行\n\n")
            sts = t  # 更新sts，用于下一天生成时间序列
    mean_perma = statistics.mean(perma_list)
    std_perma = statistics.stdev(perma_list)

    mean_sds = statistics.mean(sds_list)
    std_sds = statistics.stdev(sds_list)

    mean_sas = statistics.mean(sas_list)
    std_sas = statistics.stdev(sas_list)

    mean_gwb = statistics.mean(gwb_list)
    std_gwb = statistics.stdev(gwb_list)

    rs={"perma":{"list":perma_list, "mean":mean_perma, "std":std_perma},
        "sds":{"list":sds_list, "mean":mean_sds, "std":std_sds},
        "sas":{"list":sas_list, "mean":mean_sas, "std":std_sas},
        "gwb":{"list":gwb_list, "mean":mean_gwb, "std":std_gwb}
        }
    current_time = datetime.now()
    time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')
    add_record(record_path, f"{args.experiment}最终结果：\n{rs}\n\n")
    insert_resident_daily_record(args.experiment,
                    -1,
                    sts,
                    "init结束，perma、sds、sas、gwb保存均值，他们的detail保存标准差",
                    mean_perma,
                    std_perma,
                    mean_sds,
                    std_sds,
                    mean_sas,
                    std_sas,
                    mean_gwb,
                    std_gwb,
                    "",
                    -1,
                    "init_test",
                    "init_test",
                    agent.name,
                    time_str)
    return rs

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--experiment', help='实验名字', default='test_default')
    parser.add_argument('-d', '--days', type=int, help='实验天数', default=5)
    parser.add_argument('-rmp', '--resident_mean_perma', type=float, help='居民日常perma的均值', default=5)
    parser.add_argument('-rsp', '--resident_std_perma', type=float, help='居民日常perma的标准差', default=0.5)
    parser.add_argument('-sl', '--resident_std_law', type=float, help='perma低于多少个标准差要去看医生', default=1)
    parser.add_argument('-fd', '--forget_day', type=int, help='多少天重置医生建议', default=1)
    parser.add_argument('-ri', '--resident_id', type=int, help='居民id', default=1)
    parser.add_argument('-pp', '--prompt_path', help="prompt模板所在的地方，默认是./prompt_template，鲁棒性实验可更换这个路径", default="./prompt_template")
    args = parser.parse_args()
    perma_mean=args.resident_mean_perma
    perma_std=args.resident_std_perma
    perma_law=perma_mean-perma_std*args.resident_std_law
    
    experiment_name=args.experiment
    agent=init_agent(args.experiment, args.resident_id, perma_mean, perma_std, perma_law, args.prompt_path)
    days=args.days
    record_path=f"./record/{args.experiment}.txt"
    rs=asyncio.run(test_init_perma(record_path, agent, args, days=days))
    
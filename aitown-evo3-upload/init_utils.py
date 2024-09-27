from resident_agent import ResidentAgent
from doctor_agent import DoctorAgent

from mysql_operation import *
def init_agent(experiment_name, id, perma_mean, perma_std, perma_law, prompt_path="./prompt_template"):
    #初始化一个居民agent和一个医生agent
    rs=query_resident_info_by_id(id)
    name=rs[0]
    age=rs[1]
    job=rs[2]
    personality=rs[3]
    health=rs[4]
    perma=rs[5]
    mood=rs[6]
    relationship=rs[7]
    hobby=rs[8]
    daily_requirement=rs[9]
    default_plan=rs[10]
    preference_on_suggestions=rs[11]
    memory_path=f"./chromadb/{experiment_name}/"
    sas="未知"
    sds="未知"
    gwb="未知"
    behavior=rs[12]
    agent=ResidentAgent(name, age, job, personality, health, 
                    perma, sds, sas, gwb, mood, relationship, hobby, daily_requirement, default_plan,
                    memory_path, prompt_path, preference_on_suggestions,behavior, perma_mean, perma_std, perma_law)
    return agent

def init_doctor(experiment_name, id):
    rs=query_doctor_info_by_id(id)
    name=rs[0]
    age=rs[1]
    personality=rs[2]
    style=rs[3]
    prompt_template="./prompt_template"
    memory_path=f"./chromadb/{experiment_name}/doctor/"
    doctor_agent=DoctorAgent(name, age, personality, style, prompt_template, memory_path)
    return doctor_agent
#测试生成时间序列，后面只需要加个日期然后做agent轮询可以实现时间步处理
from datetime import datetime, timedelta

from mysql_operation import *


def generate_time_series(start_time_str, interval_seconds, end_time_str=None):
    #生成一个时间string的list，格式为：%Y-%m-%d %H:%M:%S
    start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
    
    # 计算时间序列
    current_time = start_time
    rs=[]
    rs.append(str(current_time))
    end_time=0
    if(end_time_str==None):#默认的终止时间是一天后
        end_time=start_time+timedelta(days=1)
    else:
        end_time=datetime.strptime(end_time_str, "%Y-%m-%d %H:%M:%S")
    while True:
        #print(current_time.strftime("%Y-%m-%d %H:%M:%S"))
        current_time += timedelta(seconds=interval_seconds)
        # 这里可以设置一个条件来终止循环，例如达到某个特定时间
        if(current_time>end_time):
            break
        else:
            rs.append(str(current_time))
    return rs
    
def generate_prompt(curr_input, prompt_lib_file): 
    #这个函数是拿curr_input的参数往模板文件prompt_lib_file里面去填，以按照模板生成一套prompt

    if type(curr_input) == type("string"): 
        curr_input = [curr_input]
    curr_input = [str(i) for i in curr_input]

    f = open(prompt_lib_file, "r", encoding="utf-8")
    prompt = f.read()
    f.close()
    for count, i in enumerate(curr_input):   
        prompt = prompt.replace(f"!<INPUT {count}>!", i)
    if "<commentblockmarker>###</commentblockmarker>" in prompt: 
        prompt = prompt.split("<commentblockmarker>###</commentblockmarker>")[1]
    return prompt.strip()

if __name__ == "main":
    
    # 用户输入
    start_time_input = input("请输入起始时间（格式：YYYY-MM-DD HH:MM:SS)：")
    interval_input = int(input("请输入时间间隔（秒）："))
    
    # 生成时间序列
    rs=generate_time_series(start_time_input, interval_input)
    print(rs)
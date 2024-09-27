import mysql.connector
from mysql.connector import Error
# 数据库配置信息
host = ''
port = ''
database = ''
user = ''
password = ''
def insert_doctor_info(name, age, personality, style):
    #往数据库插入一条医生信息记录
    connection=mysql.connector.connect()
    try:
        connection = mysql.connector.connect(host=host,
                                             database=database,
                                             user=user,
                                             port=port,
                                             password=password)
        if connection.is_connected():
            db_info = connection.get_server_info()
            #print("成功连接到 MySQL 服务器，版本：", db_info)
            # 创建一个 cursor 对象
            cursor = connection.cursor()
            #插入doctor_info
            insert_query = '''INSERT INTO doctor_info (doctor_name, age, personality, style)
            VALUES (%s, %s, %s, %s)'''
            cursor.execute(insert_query, (name, age, personality, style))
            connection.commit()  # 提交事务
            print("医生数据插入成功。")
    except Error as e:
        print("连接或操作失败：", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            #print("MySQL 连接已关闭。")

def query_doctor_info_by_id(id):
    #按居民info id来查找居民所有信息
    connection=mysql.connector.connect()
    try:
        connection = mysql.connector.connect(host=host,
                                             database=database,
                                             user=user,
                                             port=port,
                                             password=password)
        if connection.is_connected():
            db_info = connection.get_server_info()
            #print("成功连接到 MySQL 服务器，版本：", db_info)
            # 创建一个 cursor 对象
            cursor = connection.cursor()
            #插入resident_info
            query = '''SELECT doctor_name, age, personality, style FROM doctor_info where doctor_info_id=%s'''
            cursor.execute(query, (id,)) 
            rs = cursor.fetchone()  # 执行查询并获取结果
            print(f"医生数据查找成功{rs}。")
            return rs
    except Error as e:
        print("连接或操作失败：", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            #print("MySQL 连接已关闭。")

def query_resident_info_by_id(id):
    #按居民名字来查找居民所有信息
    connection=mysql.connector.connect()
    try:
        connection = mysql.connector.connect(host=host,
                                             database=database,
                                             user=user,
                                             port=port,
                                             password=password)
        if connection.is_connected():
            db_info = connection.get_server_info()
            #print("成功连接到 MySQL 服务器，版本：", db_info)
            # 创建一个 cursor 对象
            cursor = connection.cursor()
            #插入resident_info
            query = '''SELECT resident_name, age, job, personality, health, perma, mood, relationship, hobby, daily_requirement, default_plan, preference_on_suggestions, behavior FROM resident_info where resident_info_id=%s'''
            cursor.execute(query, (id,)) 
            rs = cursor.fetchone()  # 执行查询并获取结果
            print(f"居民数据查找成功{rs}。")
            return rs
    except Error as e:
        print("连接或操作失败：", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            #print("MySQL 连接已关闭。")

def insert_resident_info(name, age, job, personality, health, perma, mood, relationship, hobby, daily_requirement, default_plan, preference_on_suggestions):
    #往数据库插入一条医生信息记录
    connection=mysql.connector.connect()
    try:
        connection = mysql.connector.connect(host=host,
                                             database=database,
                                             user=user,
                                             port=port,
                                             password=password)
        if connection.is_connected():
            db_info = connection.get_server_info()
            #print("成功连接到 MySQL 服务器，版本：", db_info)
            # 创建一个 cursor 对象
            cursor = connection.cursor()
            #插入resident_info
            insert_query = '''INSERT INTO resident_info (resident_name, age, job, personality, health, perma, mood, relationship, hobby, daily_requirement, default_plan, preference_on_suggestions)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            cursor.execute(insert_query, (name, age, job, personality, health, perma, mood, relationship, hobby, daily_requirement, default_plan, preference_on_suggestions))
            connection.commit()  # 提交事务
            print("居民数据插入成功。")
    except Error as e:
        print("连接或操作失败：", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            #print("MySQL 连接已关闭。")

def insert_resident_daily_record(experiment_name, day, time, action, perma, perma_detail, sds, sds_detail, sas, sas_detail, gwb, gwb_detail, mood, medical_id, need_help, need_help_reason, resident_name, create_time):
    #往数据库插入一条居民活动信息记录
    connection=mysql.connector.connect()
    try:
        connection = mysql.connector.connect(host=host,
                                             database=database,
                                             user=user,
                                             port=port,
                                             password=password)
        if connection.is_connected():
            db_info = connection.get_server_info()
            #print("成功连接到 MySQL 服务器，版本：", db_info)
            # 创建一个 cursor 对象
            cursor = connection.cursor()
            #插入resident_info
            insert_query = '''INSERT INTO resident_daily_record (experiment_name, day, time, action, perma, perma_detail, sds, sds_detail, sas, sas_detail, gwb, gwb_detail, mood, medical_id, need_help, need_help_reason, resident_name, create_time)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s, %s, %s)'''
            cursor.execute(insert_query, (experiment_name, day, time, action, perma, perma_detail, sds, sds_detail, sas, sas_detail, gwb, gwb_detail, mood, medical_id, need_help, need_help_reason, resident_name, create_time))
            connection.commit()  # 提交事务
            print("居民日常活动数据插入成功。")
    except Error as e:
        print("连接或操作失败：", e)
        #print(f"连接问题debug：{perma_detail}")
    finally:
        if connection.is_connected():
            new_id = cursor.lastrowid
            cursor.close()
            connection.close()
            return new_id
            #print("MySQL 连接已关闭。")

def insert_medical_record(experiment_name, daily_record_id, doctor_question, resident_reply, suggestion, suggestion_reason, perma_pre, perma_post, perma_post_detail, mood_pre, mood_post, resident_accept, resident_accept_reason, resident_name):
    #往数据库插入一条医生信息记录
    connection=mysql.connector.connect()
    try:
        connection = mysql.connector.connect(host=host,
                                             database=database,
                                             user=user,
                                             port=port,
                                             password=password)
        if connection.is_connected():
            db_info = connection.get_server_info()
            #print("成功连接到 MySQL 服务器，版本：", db_info)
            # 创建一个 cursor 对象
            cursor = connection.cursor()
            #插入resident_info
            insert_query = '''INSERT INTO medical_record (experiment_name, daily_record_id, doctor_question, resident_reply, suggestion, suggestion_reason, perma_pre, perma_post, perma_post_detail, mood_pre, mood_post, resident_accept, resident_accept_reason, resident_name)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            cursor.execute(insert_query, (experiment_name, daily_record_id, doctor_question, resident_reply, suggestion, suggestion_reason, perma_pre, perma_post, perma_post_detail, mood_pre, mood_post, resident_accept, resident_accept_reason, resident_name))
            connection.commit()  # 提交事务
            print("居民日常活动数据插入成功。")
    except Error as e:
        print("连接或操作失败：", e)
    finally:
        if connection.is_connected():
            new_id = cursor.lastrowid
            cursor.close()
            connection.close()
            return new_id
            #print("MySQL 连接已关闭。")

def insert_god_doctor_connection(doctor_medical_record_id, experiment_name, god_medical_record_id, god_is_reference,  god_reference_reason, final_is_reference, final_reference_reason, day, time):
    connection = mysql.connector.connect()
    try:
        connection = mysql.connector.connect(host = host, database = database, user = user, port = port, password = password)
        if connection.is_connected():
            db_info = connection.get_server_info()
            cursor = connection.cursor()
            insert_query = '''INSERT INTO god_doctor_connection (doctor_medical_record_id, experiment_name, god_medical_record_id, god_is_reference,  god_reference_reason, final_is_reference, final_reference_reason, day, time)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            cursor.execute(insert_query, (doctor_medical_record_id, experiment_name, god_medical_record_id, god_is_reference,  god_reference_reason, final_is_reference, final_reference_reason, day, time))
            connection.commit()
            print("插入god和doctor连接成功")
    except Error as e:
        print("连接或操作失败：", e)
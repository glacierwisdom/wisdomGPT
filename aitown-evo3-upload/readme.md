#Requirements

The running environment of this work is described in requiremnts.txt, you can simply run the command below.

pip install -r requirements.txt

#Predecessor Work

##1. add your api to the code

1.1 After you finish preparing the running environment, you can follow the procedure below to add the api to the code:

Replace your api_key and base_url in the following code which locates in llm.py.

def get_response(text, system_setting="You are a helpful assistant."):

    client = OpenAI(

        api_key="your api key",

        base_url="your base url",  

    )

1.2 In the proposed work, we use Qwen model to get embedding. if you also use Qwen model, you fill your dashscope_api_key in the line 31 of memory1.py:

self.embedding_function = DashScopeEmbeddings(dashscope_api_key="your_dash_scope_embedding")

If you want to try other embedding function you can also replace the line 31 of memory1.py to construct a new self.embedding_function.

##2.  Setup a Mysql Database

2.1 Create a mysql database and run the sql in aitown_test.sql to setup 5 tables. Then  you can import the data in doctor_info.csv and resident_info.csv into the corresponding tables. Alternatively, you can choose to fill the description which you will use to establish the residents and experts in the Table resident_info and Table doctor_info.

Here are some description of the tables:

resident_info : the information of resident agent, you can setup your own resident agent by simply insert a new row.

doctor_info : the information of expert agent, you can setup your own expert agent by simply insert a new row.

resident_daily_record : records of resident daily life.

medical_record : if a resident go to see an expert for help, the information of the medical procedure will be recorded here. 

god_doctor_connection : during a medical procedure, the god agent will give suggestion to doctor agents. So, we set an Table god_doctor_connection to mark them.

2.2 Fill the database infomation in the line of mysql_operation.py:

host = ''

port = ''

database = ''

user = ''

password = ''

#Run the experiment

##Run a resident daily life experiment or a robustness experiment(without expert system)

python test_init.py (your parameters here)

Parameters:

-e : name of experiment, which will be used to name the log txt in ./log and record txt in ./record. In addition, we can also use it to find the output of this experiment in mysql database. 

-d : how many days you want the resident to experience

-ri : resident_info_id of the resident agent you want to use, you can find it in Table resident_info.

-pp : prompt_path, default ="./prompt_template", you can change it when you implement a robustness experiment.("./prompt_template_different_question_order", "./prompt_template_different_way_and_order", "./prompt_template_different_way4question")

##Run an experiment with expert system

Replace the number in line 467 - line 470 with your own doctor agents' id(doctor_info_id in Table doctor_info):

    doctor1 = init_doctor(args.experiment, 2)

    doctor2 = init_doctor(args.experiment, 3)

    doctor3 = init_doctor(args.experiment, 4)

    doctor4 = init_doctor(args.experiment, 6)

python main.py (your parameters here)

Parameters:

-e : name of experiment

-d : how many days you want the resident to experience

-rmp : resident_mean_perma obtained by running the test_init.py

-rsp : resident_std_perma obtained by running the test_init.py

-sl : resident_std_law, if the perma of a resident agent is lower than resident_mean_perma-resident_std_perma*resident_std_law, then this resident should seek for help.

-fd : forget_day, how many days a resident should forget the former advice from expert system.

-ri : resident_info_id of the resident agent you want to use, you can find it in Table resident_info.

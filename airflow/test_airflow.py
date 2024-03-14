from datetime import datetime
import sys
import os
print(os.path.dirname(__file__)[:-10])
sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)))

sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)[:-10]))
# sys.path.append('..')

from airflow.models.dag import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

from a import FetchHitsTaskSRCDailyTask, ParseHitsODSDailyTask

# print(AAA)

# from tasks.source.fetch_hits import (
#     FetchHitsTaskSRCDailyTask,
# )
from infra.database import Database
import datetime as dt


# def config_airflow():



# A DAG represents a workflow, a collection of tasks
with DAG(dag_id="main-dag", start_date=datetime(2024, 3, 10), schedule="0 0 * * *") as dag:
    # Tasks are represented as operators
    
    db = Database()
    db.connect()
    DATE = dt.datetime(2024, 2, 8)


    hello = BashOperator(task_id="hello", bash_command="sleep 5")

    @task()
    def FetchHits():
        # print("hjujhuh")
        FetchHitsTaskSRCDailyTask(db.get_client()).run(DATE)
    
    @task()
    def ParseHits():
        # print("hjujhuh")
        ParseHitsODSDailyTask(db.get_client()).run(DATE)

    # Set dependencies between tasks
    hello >> FetchHits() >> ParseHits()

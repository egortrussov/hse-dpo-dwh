from datetime import datetime
import sys
import os

from airflow.models.dag import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tasks.source.fetch_hits import (
    FetchHitsTaskSRCDailyTask,
)
from tasks.ods.parse_hits import (
    ParseHitsODSDailyTask,
)
from tasks.ods.first_visits import (
    FirstVisitsODSDailyTask,
)
from tasks.dds.search_events import (
    SearchEventsDDSDailyTask
)
from tasks.dds.program_views import (
    ProgramViewEventDDSDailyTask,
)
from tasks.cdm.conversion_cube import (
    ConversionCubeCDMDailyTask,
)
from tasks.dds.programs_meta import (
    ProgramsMetaDDSTask
)
from tasks.dds.hits_enriched import (
    HitsEnrichedDDSDailyTask,
)

from tasks.source.fetch_visits import (
    FetchVisitsSRCDailyTask,
)
from tasks.ods.parse_visits import (
    ParseVisitsODSDailyTask,
)
from tasks.dds.achieved_goals import (
    AchievedGoalsDDSDailyTask,
)
from tasks.cdm.hits_enriched_mart import (
    HitsEnrichedCumulativeDailyTask
)


# from tasks.source.fetch_hits import (
#     FetchHitsTaskSRCDailyTask,
#     ParseHitsODSDailyTask,
# )
from infra.database import Database
import datetime as dt



# def config_airflow():



# A DAG represents a workflow, a collection of tasks
with DAG(dag_id="main-dag", start_date=datetime(2024, 3, 20), schedule="0 0 * * *") as dag:
    # Tasks are represented as operators
    
    db = Database()
    db.connect()
    # DATE = dt.datetime(2024, 2, 9)
    DATE = dt.datetime.now() - dt.timedelta(days=1)


    hello = BashOperator(task_id="hello", bash_command="sleep 5")
    hello1 = BashOperator(task_id="hello1", bash_command="sleep 5")
    hello2 = BashOperator(task_id="hello2", bash_command="sleep 5")


    @task()
    def FetchHits():
        # print("hjujhuh")
        FetchHitsTaskSRCDailyTask(db.get_client()).run(DATE)
    
    @task()
    def FetchVisits():
        # print("hjujhuh")
        FetchVisitsSRCDailyTask(db.get_client()).run(DATE)
    
    @task()
    def ParseHits():
        ParseHitsODSDailyTask(db.get_client()).run(DATE)
        
    @task()
    def ParseVisits():
        # print("hjujhuh")
        ParseVisitsODSDailyTask(db.get_client()).run(DATE)
    
    @task()
    def CalculateFirstVisits():
        FirstVisitsODSDailyTask(db.get_client()).run(DATE)
    
    @task()
    def EnrichHits():
        HitsEnrichedDDSDailyTask(db.get_client()).run(DATE)
    
    @task()
    def ProgramViewEvents():
        ProgramViewEventDDSDailyTask(db.get_client()).run(DATE)
    
    @task()
    def SearchEvents():
        SearchEventsDDSDailyTask(db.get_client()).run(DATE)
    
    @task()
    def AchievedGoals():
        AchievedGoalsDDSDailyTask(db.get_client()).run(DATE)
    
    @task()
    def ConversionCube():
        ConversionCubeCDMDailyTask(db.get_client()).run(DATE)
    
    @task()
    def HitsEnrichedMart():
        HitsEnrichedCumulativeDailyTask(db.get_client()).run(DATE)

    # Set dependencies between tasks]
    # hello >> FetchHits() >> ParseHits()
    hello >> \
        [FetchHits() >> ParseHits()] >> \
        hello1 >> \
        [FetchVisits() >> ParseVisits()] >> \
        hello2 >> \
        [CalculateFirstVisits(), EnrichHits(), ProgramViewEvents(), SearchEvents(), AchievedGoals()] >> \
        ConversionCube() >> HitsEnrichedMart()
    # ParseHits() >> CalculateFirstVisits()
    # ParseHits() >> EnrichHits()
    
    

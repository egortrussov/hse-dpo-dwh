import datetime as dt
from infra.garbage_collector import GarbageCollector
from infra.garbage_collector.logtypes_config import (
    GC_LOGTYPES_WATCH_LIST,
)
from infra.database import Database

db = Database()
db.connect()

class Task:

    def __init__(self, client, runner_function):
        self.client = client
        self.runner_function = runner_function
        
        self.__config_gc()

    def configure_deps(self, inputs, outputs):
        self._dependencies = {
            "inputs": inputs,
            "outputs": outputs,
        }


    def get_depencencies(self):
        return self._dependencies


    def run(self, task_date = None, **kwargs):
        if task_date is None:
            task_date = dt.datetime.now()

        self.runner_function(
            self.client,
            self.get_depencencies()["inputs"],
            self.get_depencencies()["outputs"],
            task_date=task_date,
            **kwargs,
        )

        self.gc.collect()
    
    def __config_gc(self):
        self.gc = GarbageCollector(db, GC_LOGTYPES_WATCH_LIST)

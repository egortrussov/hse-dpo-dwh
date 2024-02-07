from infra import (
    Task,
)
from .run import run
import logs as logs


class FetchHitsTaskSRCDailyTask(Task):

    def __init__(self, client):
        super().__init__(
            client=client,
            runner_function=run,
        )
        super().configure_deps(
            inputs={},
            outputs={
                "hits": logs.HitsLogSource1d,
            },
        )
    
    def run(self, task_date):
        super().run(task_date=task_date)

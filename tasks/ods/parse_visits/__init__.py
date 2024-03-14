from infra import (
    Task,
)
from .run import run
import logs as logs


class ParseVisitsODSDailyTask(Task):

    def __init__(self, client):
        super().__init__(
            client=client,
            runner_function=run,
        )
        super().configure_deps(
            inputs={
                "source_visits": logs.VisitsLogSource1d,
            },
            outputs={
                "parsed_visits": logs.VisitsParsedODS1d,
            },
        )

    def run(self, task_date):
        super().run(task_date=task_date)

from infra import (
    Task,
)
from .run import run
import logs as logs


class AchievedGoalsDDSDailyTask(Task):

    def __init__(self, client):
        super().__init__(
            client=client,
            runner_function=run,
        )
        super().configure_deps(
            inputs={
                "visits": logs.VisitsParsedODS1d,
            },
            outputs={
                "goals": logs.AchievedGoalsDDS1d,
            },
        )

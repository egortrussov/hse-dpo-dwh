from infra import (
    Task,
)
from .run import run
import logs as logs


class ProgramViewEventDDSDailyTask(Task):

    def __init__(self, client):
        super().__init__(
            client=client,
            runner_function=run,
        )
        super().configure_deps(
            inputs={
                "visits": logs.HitsLogParsedODS1d,
            },
            outputs={
                "program_views": logs.ProgramPageViewsDDS1d,
            },
        )

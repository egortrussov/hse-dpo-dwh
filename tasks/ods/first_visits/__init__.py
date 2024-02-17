from infra import (
    Task,
)
from .run import run
import logs as logs


class FirstVisitsODSDailyTask(Task):

    def __init__(self, client):
        super().__init__(
            client=client,
            runner_function=run,
        )
        super().configure_deps(
            inputs={
                "previous_first_visits": logs.FirstVisitsODS1d,
                "new_visits": logs.HitsLogParsedODS1d,
                "first_visits_cumulative": logs.FirstVisitsCumulative,
            },
            outputs={
                "first_visits": logs.FirstVisitsODS1d,
                "first_visits_cumulative": logs.FirstVisitsCumulative,
            },
        )

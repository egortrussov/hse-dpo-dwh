from infra import (
    Task,
)
from .run import run
import logs as logs


class ConversionCubeCDMDailyTask(Task):

    def __init__(self, client):
        super().__init__(
            client=client,
            runner_function=run,
        )
        super().configure_deps(
            inputs={
                "visits": logs.HitsLogParsedODS1d,
                "first_visits": logs.FirstVisitsODS1d,
                "search_events": logs.SearchEventsDDS1d,
                "program_views": logs.ProgramPageViewsDDS1d,
                "goals": logs.AchievedGoalsDDS1d,
            },
            outputs={
                "conversion_cube": logs.ConversionCubeCDM1d,
                "conversion_cube_cumulative": logs.ConversionCumulativeLog
            },
        )

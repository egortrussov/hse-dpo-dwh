from infra import (
    Task,
)
from .run import run
import logs as logs


class HitsEnrichedCumulativeDailyTask(Task):

    def __init__(self, client):
        super().__init__(
            client=client,
            runner_function=run,
        )
        super().configure_deps(
            inputs={
                "dds_hits": logs.HitsEnrichedLogDDS1d,
            },
            outputs={
                "hits_enriched": logs.HitsEnrichedCumulativeLog,
            },
        )

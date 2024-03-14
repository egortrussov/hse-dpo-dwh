from infra import (
    Task,
)
from .run import run
import logs as logs


class HitsEnrichedDDSDailyTask(Task):

    def __init__(self, client):
        super().__init__(
            client=client,
            runner_function=run,
        )
        super().configure_deps(
            inputs={
                "ods_hits": logs.HitsLogParsedODS1d,
                "programs_meta": logs.ProgramsMetadataLog,
            },
            outputs={
                "hits_enriched": logs.HitsEnrichedLogDDS1d,
            },
        )

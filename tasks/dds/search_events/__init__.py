from infra import (
    Task,
)
from .run import run
import logs as logs


class SearchEventsDDSDailyTask(Task):

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
                "search_events": logs.SearchEventsDDS1d,
            },
        )

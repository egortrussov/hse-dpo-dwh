from infra import (
    Task,
)
from .run import run
import logs as logs


class SearchPopularityDailyTask(Task):

    def __init__(self, client):
        super().__init__(
            client=client,
            runner_function=run,
        )
        super().configure_deps(
            inputs={
                "search_events": logs.SearchEventsDDS1d,
            },
            outputs={
                "search_popularity": logs.SearchPopularityLog,
            },
        )

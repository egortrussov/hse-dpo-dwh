from infra import (
    Task,
)
from .run import run
import logs as logs


class ProgramsMetaDDSTask(Task):

    def __init__(self, client):
        super().__init__(
            client=client,
            runner_function=run,
        )
        super().configure_deps(
            inputs={
            },
            outputs={
                "programs_meta": logs.ProgramsMetadataLog,
            },
        )

from tasks.source.fetch_hits import (
    FetchHitsTaskSRCDailyTask,
)
from tasks.ods.parse_hits import (
    ParseHitsODSDailyTask,
)
from tasks.ods.first_visits import (
    FirstVisitsODSDailyTask,
)
from tasks.dds.search_events import (
    SearchEventsDDSDailyTask
)
from tasks.dds.program_views import (
    ProgramViewEventDDSDailyTask,
)

from infra.database import Database

import datetime as dt

db = Database()
db.connect()

# FetchHitsTaskSRCDailyTask(db.get_client()).run(dt.datetime(2024, 1, 28))
# ParseHitsODSDailyTask(db.get_client()).run(dt.datetime(2024, 1, 28))

# FirstVisitsODSDailyTask(db.get_client()).run(dt.datetime(2024, 1, 28))

# SearchEventsDDSDailyTask(db.get_client()).run(dt.datetime(2024, 1, 28))
ProgramViewEventDDSDailyTask(db.get_client()).run(dt.datetime(2024, 1, 28))
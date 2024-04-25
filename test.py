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
from tasks.cdm.conversion_cube import (
    ConversionCubeCDMDailyTask,
)
from tasks.dds.programs_meta import (
    ProgramsMetaDDSTask
)
from tasks.dds.hits_enriched import (
    HitsEnrichedDDSDailyTask,
)

from tasks.source.fetch_visits import (
    FetchVisitsSRCDailyTask,
)
from tasks.ods.parse_visits import (
    ParseVisitsODSDailyTask,
)
from tasks.dds.achieved_goals import (
    AchievedGoalsDDSDailyTask,
)
from tasks.cdm.hits_enriched_mart import (
    HitsEnrichedCumulativeDailyTask,
)

from infra.database import Database

import datetime as dt

import clickhouse_connect

# clickhouse_connect.get_client(host='172.18.0.10')

db = Database()
db.connect()

DATE = dt.datetime(2024, 4, 4)

# FetchVisitsSRCDailyTask(db).run(DATE)
ParseVisitsODSDailyTask(db).run(DATE)

FetchHitsTaskSRCDailyTask(db).run(DATE)
ParseHitsODSDailyTask(db).run(DATE)

AchievedGoalsDDSDailyTask(db).run(DATE)


ProgramsMetaDDSTask(db).run(DATE)

HitsEnrichedDDSDailyTask(db).run(DATE)

FirstVisitsODSDailyTask(db).run(DATE)

# SearchEventsDDSDailyTask(db).run(DATE)
# ProgramViewEventDDSDailyTask(db).run(DATE)

# ConversionCubeCDMDailyTask(db).run(DATE)
# HitsEnrichedCumulativeDailyTask(db).run(DATE)

from infra.database import Database

import datetime as dt

import clickhouse_connect

from logs import (
    AchievedGoalsDDS1d,
)

from infra.garbage_collector import GarbageCollector

db = Database()
db.connect()

gc = GarbageCollector(db, [
    AchievedGoalsDDS1d
])

gc.collect()
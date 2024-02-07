from infra import (
    PermanentLogType,
    LogTypeWithTTL,
    StaticLogType,
)

FirstVisitsODS1d = LogTypeWithTTL(
    database="conversion",
    name="first_visits",
    ttl=3,
    fields=[
        "client_id",
        "msk_date",
        "datetime",
    ],
    fields_types=["String"] * 3,
    engine="Log",
)

SearchEventsDDS1d = LogTypeWithTTL(
    database="conversion",
    name="search",
    ttl=3,
    fields=[
        "client_id",
        "msk_date",
        "tags",
        "types",
        "queries",
    ],
    fields_types=[
        "String",
        "String",
        "Array(String)",
        "Array(String)",
        "Array(String)",
    ],
    engine="Log",
)


ProgramPageViewsDDS1d = LogTypeWithTTL(
    database="conversion",
    name="program_views",
    ttl=3,
    fields=[
        "client_id",
        "msk_date",
        "program_ids",
        "programs_count",
    ],
    fields_types=[
        "String",
        "String",
        "Array(String)",
        "UInt32"
    ],
    engine="Log",
)

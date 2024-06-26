from infra.logtypes import (
    LogTypeWithTTL,
    PermanentLogType,
)
from infra.database import (
    Field,
)

FirstVisitsODS1d = LogTypeWithTTL(
    database="ods_first_visits",
    name="first_visits",
    ttl=3,
    fields_list=[
        Field("client_id", "String", str),
        Field("msk_date", "String", str),
        Field("datetime", "String", str),
    ],
    engine="Log",
)

FirstVisitsCumulative = LogTypeWithTTL(
    database="ods_first_visits",
    name="first_visits_cumulative",
    ttl=3,
    fields_list=[
        Field("client_id", "String", str),
        Field("msk_date", "String", str),
        Field("datetime", "String", str),
    ],
    engine="Log",
)

SearchEventsDDS1d = LogTypeWithTTL(
    database="dds_search_events",
    name="search",
    ttl=3,
    fields_list=[
        Field("client_id", "String", str),
        Field("msk_date", "String", str),
        Field("tags", "Array(String)", list),
        Field("types", "Array(String)", list),
        Field("queries", "Array(String)", list),
    ],
    engine="Log",
)

ProgramPageViewsDDS1d = LogTypeWithTTL(
    database="dds_program_views",
    name="program_views",
    ttl=3,
    fields_list=[
        Field("client_id", "String", str),
        Field("msk_date", "String", str),
        Field("program_ids", "Array(String)", list),
        Field("programs_count", "UInt32", list),
    ],
    engine="Log",
)

AchievedGoalsDDS1d = LogTypeWithTTL(
    database="dds_achieved_goals",
    name="goals",
    ttl=3,
    fields_list=[
        Field("client_id", "String", str),
        Field("msk_date", "String", str),
        Field("goal", "Nullable(String)", list),
        Field("goal_name", "Nullable(String)", list),
        Field("visit_param_goal", "Nullable(String)", list),
        Field("visit_param_goal_rus", "Nullable(String)", list),
        Field("visit_param_goal_program_id", "Nullable(String)", list),
    ],
    engine="Log",
)

ConversionCubeCDM1d = PermanentLogType(
    database="cdm_conversion_cube",
    name="conversion_cube",
    fields_list=[
        Field("action", "String", str),
        Field("msk_date", "String", str),
        Field("client_id", "String", str),

        Field("tags", "Array(Nullable(String))", list),
        Field("types", "Array(String)", list),
        Field("queries", "Array(String)", list),

        Field("program_ids", "Array(String)", list),
        Field("programs_count", "Nullable(UInt32)", list),

        Field('utm_campaign', "Nullable(String)", str),
        Field('utm_content', "Nullable(String)", str),
        Field('utm_medium', "Nullable(String)", str),
        Field('utm_source', "Nullable(String)", str),
        Field('country', "Nullable(String)", str),
        Field('city', "Nullable(String)", str),
        Field('os_family', "Nullable(String)", str),
        Field('device_type', "Nullable(String)", str),
    ]
)

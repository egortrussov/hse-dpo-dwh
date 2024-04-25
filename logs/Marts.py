from infra.logtypes import (
    PermanentLogType,
    StaticLogType,
)
from infra.database import (
    Field,
)


SearchPopularityLog = StaticLogType(
    database="cdm",
    name="search_popularity",
    fields_list=[
        Field("msk_date", "String", str),
        Field("search_type", "String", str),
        Field("search_value", "String", str),
        Field("count", "UInt32", int),
    ],
)

HitsEnrichedCumulativeLog = StaticLogType(
    database="cdm",
    name="hits_enriched",
    fields_list=[
        Field('watch_id', "Nullable(String)", str),
        Field('client_id', "Nullable(String)", str),
        Field('msk_date', "Nullable(String)", str),
        Field('datetime', "Nullable(String)", str),
        Field('url', "Nullable(String)", str),
        Field('page_title', "Nullable(String)", str),
        Field('utm_campaign', "Nullable(String)", str),
        Field('utm_content', "Nullable(String)", str),
        Field('utm_medium', "Nullable(String)", str),
        Field('utm_source', "Nullable(String)", str),
        Field('country', "Nullable(String)", str),
        Field('city', "Nullable(String)", str),
        Field('os_family', "Nullable(String)", str),
        Field('device_type', "Nullable(String)", str),
        Field('from', "Nullable(String)", str),
        Field('ip', "Nullable(String)", str),
        Field('page_type', "Nullable(String)", str),
        Field('page_subtype', "Nullable(String)", str),
        Field('program_id', "Nullable(String)", str),
        Field('search_query', "Nullable(String)", list),
        Field('search_tags', "Array(Nullable(String))", list),
        Field('search_types', "Array(Nullable(String))", list),

        Field('program_title', "Nullable(String)", str),
        Field('program_type', "Nullable(String)", str),
        Field('program_org_unit_id', "Nullable(String)", str),
        Field('program_org_unit_title', "Nullable(String)", str),
    ]
)

VisitsParsedCumulativeLog = StaticLogType(
    database="cdm",
    name="visits",
    fields_list=[
        Field("visit_id", "Nullable(String)", str),
        Field("client_id", "Nullable(String)", str),
        Field("watch_ids", "Nullable(String)", str),
        Field("msk_date", "Nullable(String)", str),
        Field("parsed_params_key_1", "Nullable(String)", str),
        Field("parsed_params_key_2", "Nullable(String)", str),
        Field("parsed_params_key_3", "Nullable(String)", str),
        Field("parsed_params_key_4", "Nullable(String)", str),
        Field("parsed_params_key_5", "Nullable(String)", str),
        Field("goals_id", "Nullable(String)", str),
        Field("ip", "Nullable(String)", str),
        Field("country", "Nullable(String)", str),
        Field("city", "Nullable(String)", str),
        Field("first_traffic_source", "Nullable(String)", str),
        Field("last_traffic_source", "Nullable(String)", str),
        Field("utm_source", "Nullable(String)", str),
        Field("utm_campaign", "Nullable(String)", str),

        Field("visit_param_goal", "Nullable(String)", str),
        Field("visit_param_goal_rus", "Nullable(String)", str),
        Field("visit_param_goal_program_id", "Nullable(String)", str),
        
        Field("goal", "Nullable(String)", str),
        Field("goal_name", "Nullable(String)", str),
    ],
)


ConversionCumulativeLog = StaticLogType(
    database="cdm",
    name="conversion",
    fields_list=[
        Field("action", "String", str),
        Field("msk_date", "String", str),
        Field("client_id", "String", str),

        # Field("main_program_id", "Nullable(String)", str),
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

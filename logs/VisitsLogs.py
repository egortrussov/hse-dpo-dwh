# from infra import (
#     PermanentLogType,
# )
from infra.logtypes import (
    PermanentLogType,
    LogTypeWithTTL,
)
from infra.database import (
    Field,
)

VisitsLogSource1d = LogTypeWithTTL(
    database="source_visits",
    name="visits",
    ttl=30,
    fields_list=[
        Field("visitID", "Nullable(String)", str),
        Field("clientID", "Nullable(String)", str),
        Field("watchIDs", "Nullable(String)", str),
        Field("date", "Nullable(String)", str),
        Field("parsedParamsKey1", "Nullable(String)", str),
        Field("parsedParamsKey2", "Nullable(String)", str),
        Field("parsedParamsKey3", "Nullable(String)", str),
        Field("parsedParamsKey4", "Nullable(String)", str),
        Field("parsedParamsKey5", "Nullable(String)", str),
        Field("goalsID", "Nullable(String)", str),
        Field("ipAddress", "Nullable(String)", str),
        Field("regionCountry", "Nullable(String)", str),
        Field("regionCity", "Nullable(String)", str),
        Field("firstTrafficSource", "Nullable(String)", str),
        Field("lastTrafficSource", "Nullable(String)", str),
        Field("lastsignUTMSource", "Nullable(String)", str),
        Field("lastsignUTMCampaign", "Nullable(String)", str),
    ],
)

VisitsParsedODS1d = LogTypeWithTTL(
    database="ods_visits",
    name="visits",
    ttl=14,
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

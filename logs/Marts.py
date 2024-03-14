from infra.logtypes import (
    PermanentLogType,
    StaticLogType,
)
from infra.database import (
    Field,
)


SearchPopularityLog = PermanentLogType(
    database="conversion",
    name="search_popularity",
    fields_list=[
        Field("msk_date", "String", str),
        Field("search_type", "String", str),
        Field("search_value", "String", str),
        Field("count", "UInt32", int),
    ],
)

ConversionCumulativeLog = StaticLogType(
    database="conversion",
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

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

HitsEnrichedCumulativeLog = StaticLogType(
    database="conversion",
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

        Field('program_title', "String", str),
        Field('program_type', "String", str),
        Field('program_org_unit_id', "String", str),
        Field('program_org_unit_title', "String", str),
    ]
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

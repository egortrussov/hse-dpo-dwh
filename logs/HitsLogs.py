# from infra import (
#     PermanentLogType,
# )
from infra.logtypes import (
    PermanentLogType,
)
from infra.database import (
    Field,
)

HitsLogSource1d = PermanentLogType(
    database="source_hits",
    name="hits",
    fields_list=[
        Field("watchID", "String", str),
        Field("clientID", "String", str),
        Field("date", "String", str),
        Field("dateTime", "String", str),
        Field("URL", "String", str),
        Field("title", "String", str),
        Field("UTMCampaign", "String", str),
        Field("UTMContent", "String", str),
        Field("UTMMedium", "String", str),
        Field("UTMSource", "String", str),
        Field("regionCountry", "String", str),
        Field("regionCity", "String", str),
        Field("operatingSystemRoot", "String", str),
        Field("deviceCategory", "String", str),
        Field("from", "String", str),
        Field("ipAddress", "String", str),
    ],
)

HitsLogParsedODS1d = PermanentLogType(
    database="ods_hits",
    name="hits",
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
    ],
)


# HitsLogSource1d = PermanentLogType(
#     database="source_hits",
#     name="hits",
#     fields=[
#         "watchID",
#         "clientID",
#         "date",
#         "dateTime",
#         "URL",
#         "title",
#         "UTMCampaign",
#         "UTMContent",
#         "UTMMedium",
#         "UTMSource",
#         "regionCountry",
#         "regionCity",
#         "operatingSystemRoot",
#         "deviceCategory",
#         "from",
#         "ipAddress"
#     ],
#     fields_types=["String"] * 16,
# )

# HitsLogParsedODS1d = PermanentLogType(
#     database="ods_hits",
#     name="hits",
#     fields=[
#         'watch_id',
#         'client_id',
#         'msk_date',
#         'datetime',
#         'url',
#         'page_title',
#         'utm_campaign',
#         'utm_content',
#         'utm_medium',
#         'utm_source',
#         'country',
#         'city',
#         'os_family',
#         'device_type',
#         'from',
#         'ip',
#         'page_type',
#         'page_subtype',
#         'program_id',
#         'search_query',
#         'search_tags',
#         'search_types',
#     ],
#     fields_types=["Nullable(String)"] * 20 + [
#         "Array(Nullable(String))",
#         "Array(Nullable(String))",
#     ],
# )

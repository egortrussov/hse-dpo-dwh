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

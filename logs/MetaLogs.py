from infra.logtypes import (
    StaticLogType,
)
from infra.database import (
    Field,
)

ProgramsMetadataLog = StaticLogType(
    database="dds_metadata",
    name="programs",
    fields_list=[
        Field("id", "Nullable(String)", str),
        Field("url", "Nullable(String)", str),
        Field("title", "Nullable(String)", str),
        Field("description", "Nullable(String)", str),
        Field("duration", "Nullable(String)", str),
        Field("type", "Nullable(String)", str),
        Field("study_format", "Nullable(String)", str),
        Field("org_unit_id", "Nullable(String)", str),
        Field("org_unit_title", "Nullable(String)", str),
        Field("external_application_form_url", "Nullable(String)", str),
        Field("application_form_url", "Nullable(String)", str),
        Field("external_ask_form_url", "Nullable(String)", str),
        Field("ask_form_url", "Nullable(String)", str),
    ]
)

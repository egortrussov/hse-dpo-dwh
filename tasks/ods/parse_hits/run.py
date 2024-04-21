from infra import (
    LogsFetcher,
    save_data_to_log,
)
from infra.table_container import (
    TableContainer,
)
from infra.query_sender import (
    send_select_query,
)
from infra.table_processing import (
    represent_table_as_list_of_dicts,
)
from datetime import datetime
from .utils import (
    RAW_HITS_FILTER,
    rename_fields,
    get_page_type,
    get_page_subtype,
    get_query_param_value,
    get_page_program_id,
)

def run(client, inputs, outputs, task_date: datetime):
    task_date_normalized = task_date.isoformat()[:10]
    input_table = inputs["source_hits"].get_table_name_by_date(task_date_normalized)

    table = send_select_query(
        client.get_client(),
        inputs["source_hits"],
        task_date_normalized,
        fields=None,
        filters=RAW_HITS_FILTER,
    )

    table.rename_fields(
        watchID="watch_id",
        clientID="client_id",
        date="msk_date",
        dateTime="datetime",
        URL="url",
        title="page_title",
        UTMCampaign="utm_campaign",
        UTMContent="utm_content",
        UTMMedium="utm_medium",
        UTMSource="utm_source",
        regionCountry="country",
        regionCity="city",
        operatingSystemRoot="os_family",
        deviceCategory="device_type",
        ipAddress="ip",
    )

    table.map_rows(parse_row)

    table.save_data_to_log(
        client.get_client(),
        outputs["parsed_hits"],
        task_date_normalized,
    )


def parse_row(row):
    row["page_type"] = get_page_type(row["url"])
    row["page_subtype"] = get_page_subtype(row["url"])

    row["search_tags"] = get_query_param_value(row["url"], "tags")
    row["search_query"] = get_query_param_value(row["url"], "query")
    row["search_types"] = get_query_param_value(row["url"], "types")

    row["program_id"] = get_page_program_id(row["page_type"], row["url"])

    return row
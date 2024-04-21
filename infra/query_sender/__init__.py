from infra.logtypes.logtype_base import LogTypeBase
from infra.table_container import (
    TableContainer,
)


def send_query(
        client,
        query,
):
    client.query(query)


def send_select_query(
        client,
        log_type: LogTypeBase,
        date_str: str,
        fields: list[str] = None,
        filters: str = None
) -> TableContainer:
    fields_str = ""

    if fields is None:
        fields_str = "*"
    else:
        for field in fields:
            if field not in log_type.fields:
                raise Exception(f"Unknown field {field} in logtype {log_type.get_table_name_by_date(date_str)}")
            if fields_str != "":
                fields_str += ",\n" 
            fields_str += field
        fields_str += "\n"

    query = f"""
        SELECT
            { fields_str }
        FROM
            { log_type.get_table_name_by_date(date_str) }
        { "" if filters is None else "WHERE" + filters }
    """

    result = client \
        .query(query)

    return TableContainer(
        result.column_names,
        result.result_rows,
    )

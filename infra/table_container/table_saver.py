from infra.logtypes.logtype_base import (
    LogTypeBase,
)


def save_data_to_log(
        client,
        log_type: LogTypeBase,
        data,
        date,
):
    print(f"Saving { len(data) } rows to table " + log_type.get_table_name_by_date(date))

    client.query(
        f"CREATE DATABASE IF NOT EXISTS {log_type.get_database()}"
    )
    
    drop_table_query = f"""
        DROP TABLE IF EXISTS
        { log_type.get_table_name_by_date(date) }
    """

    client.command(drop_table_query)

    print("Dropped table")

    create_table_query = f"""
        CREATE TABLE IF NOT EXISTS
        { log_type.get_table_name_by_date(date) }
        (
            { log_type.get_fields_list_with_types() }
        )
        ENGINE { log_type.get_engine() }
    """

    client.command(create_table_query)

    print("Created table")

    for i in range(1, len(data) // 500 + 1):
        print("Inserting batch", i)
        print(len(data[(i - 1) * 500: i * 500]))
        client.insert(
            log_type.get_table_name_by_date(date),
            data[(i - 1) * 500: i * 500],
            column_names=log_type.get_fields(),
        )
        print("Successfully inserted batch", i)

    print(f"Successfully saved { len(data) } rows to table " + log_type.get_table_name_by_date(date))

from infra import (
    LogsFetcher,
    save_data_to_log,
)
from infra.table_container import (
    TableContainer,
)
from infra.query_sender import (
    send_query,
)
from infra.database import Database
from datetime import datetime, timedelta
from .utils import (
    FIELDS,
    get_first_visits_query,
    get_first_visits_query1,
)

db = Database()
db.connect()

def run(client, inputs, outputs, task_date: datetime, mode=None):
    task_date_normalized = task_date.isoformat()[:10]

    yesterday_date = task_date - timedelta(days=1)
    yesterday_date_str = yesterday_date.isoformat()[:10]

    fetcher = LogsFetcher()

    if mode == "recalc":
        recalc_previous_first_visits(
            task_date,
            client,
            inputs,
            fetcher
        )

    db.create_logtype_table(outputs["first_visits"], task_date_normalized)
    db.create_logtype_table(outputs["first_visits_cumulative"], task_date_normalized)

    db.query(f"""
        INSERT INTO
            { outputs["first_visits_cumulative"].get_table_name_by_date(task_date_normalized) }
        SELECT
            client_id,
            MIN(msk_date) as msk_date,
            MIN(datetime) as datetime
        FROM (
            SELECT * FROM { inputs["first_visits_cumulative"].get_table_name_by_date(yesterday_date_str) }
            UNION ALL
            (
                SELECT
                    client_id,
                    msk_date,
                    datetime
                FROM { inputs["new_visits"].get_table_name_by_date(task_date_normalized) }
            )
        )
        GROUP BY
            client_id
    """)

    db.query(f"""
        INSERT INTO
            { outputs["first_visits"].get_table_name_by_date(task_date_normalized) }
        SELECT
            client_id,
            msk_date,
            datetime
        FROM
            { outputs["first_visits_cumulative"].get_table_name_by_date(task_date_normalized) }
        WHERE
            msk_date = '{ task_date_normalized }'
    """)



def recalc_previous_first_visits(
        current_date: datetime,
        client,
        inputs,
        fetcher: LogsFetcher,
):
    yesterday_date = current_date - timedelta(days=1)
    yesterday_date_str = yesterday_date.isoformat()[:10]

    limit_date = current_date - timedelta(days=1)
    limit_date_str = limit_date.isoformat()[:10]

    print(yesterday_date_str, limit_date_str)
    # exit(0)

    fetcher.fetch_logs(
        fields_list=FIELDS,
        date_start=limit_date_str,
        date_end=yesterday_date_str,
        logs_type="hits",
    )

    fetcher.get_rows()

    table = TableContainer(
        fetcher.get_fields(),
        fetcher.get_rows(),
    )

    table.rename_fields(
        **{
            "ym:pv:clientID": "client_id",
            "ym:pv:date": "msk_date",
            "ym:pv:dateTime": "datetime",
        }
    )

    table.save_data_to_log(
        client,
        log_type=inputs["first_visits_cumulative"],
        date=yesterday_date_str,
    )




def drop_yesterday_table(
    current_date: datetime,
    log_type,
):
    yesterday_date = current_date - timedelta(days=1)
    yesterday_date_str = yesterday_date.isoformat()[:10]

    db.drop_table(log_type, yesterday_date_str)


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


db = Database()
db.connect()

def run(client, inputs, outputs, task_date: datetime, mode=None):
    task_date_normalized = task_date.isoformat()[:10]

    db.create_logtype_table(outputs["conversion_cube"], task_date_normalized)

    db.query(f"""
        INSERT INTO
            { outputs["conversion_cube"].get_table_name_by_date(task_date_normalized) }
        SELECT *
        FROM (
            SELECT
                s.action AS action,
                s.msk_date AS msk_date,
                s.client_id AS client_id,
                [''] as tags,
                t.utm_source AS utm_source
            FROM (
                -- raw visits
                SELECT
                    'visit' AS action,
                    msk_date,
                    client_id,
                    MIN(datetime) AS datetime
                FROM
                    { inputs["visits"].get_table_name_by_date(task_date_normalized) }
                GROUP BY msk_date, client_id
                UNION ALL
                -- first visits
                SELECT
                    'first_visit' AS action,
                    msk_date,
                    client_id,
                    datetime
                FROM
                    { inputs["first_visits"].get_table_name_by_date(task_date_normalized) }
            ) AS s
            JOIN (
                SELECT
                    msk_date,
                    client_id,
                    datetime,
                    first_value(utm_source) as utm_source
                FROM
                    { inputs["visits"].get_table_name_by_date(task_date_normalized) }
                GROUP BY
                    msk_date,
                    client_id,
                    datetime
            ) AS t
            ON s.client_id = t.client_id AND s.datetime = t.datetime
        ) AS s
        UNION ALL (
            SELECT
                s.action as action,
                s.msk_date as msk_date,
                s.client_id as client_id,
                s.tags as tags,
                t.utm_source as utm_source
            from (
                SELECT
                    'search' AS action,
                    msk_date,
                    client_id,
                    tags
                FROM
                    { inputs["search_events"].get_table_name_by_date(task_date_normalized) }
                UNION ALL
                SELECT
                    'view_program' AS action,
                    msk_date,
                    client_id,
                    [] as tags
                FROM
                    { inputs["program_views"].get_table_name_by_date(task_date_normalized) }
            ) as s
            JOIN (
                SELECT
                    msk_date,
                    client_id,
                    first_value(utm_source) as utm_source
                FROM
                    { inputs["visits"].get_table_name_by_date(task_date_normalized) }
                GROUP BY
                    msk_date,
                    client_id
            ) AS t
            USING client_id, msk_date
        )
    """)

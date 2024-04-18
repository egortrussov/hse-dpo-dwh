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
                [] as tags,
                [] as types,
                [] as queries,
                [] as program_ids,
                0 as programs_count,

                t.utm_source AS utm_source,
                t.utm_campaign as utm_campaign,
                t.utm_content as utm_content,
                t.utm_medium as utm_medium,
                t.utm_source as utm_source,

                t.country as country,
                t.city as city,
                t.os_family as os_family,
                t.device_type as device_type
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
                    first_value(utm_campaign) as utm_campaign,
                    first_value(utm_content) as utm_content,
                    first_value(utm_medium) as utm_medium,
                    first_value(utm_source) as utm_source,

                    first_value(country) as country,
                    first_value(city) as city,
                    first_value(os_family) as os_family,
                    first_value(device_type) as device_type
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
                s.types as types,
                s.queries as queries,
                s.program_ids as program_ids,
                s.programs_count as programs_count,

                t.utm_campaign as utm_campaign,
                t.utm_content as utm_content,
                t.utm_medium as utm_medium,
                t.utm_source as utm_source,

                t.country as country,
                t.city as city,
                t.os_family as os_family,
                t.device_type as device_type
            from (
                -- search events
                SELECT
                    'search' AS action,
                    msk_date,
                    client_id,
                    tags,
                    types,
                    queries,
                    [] as program_ids,
                    0 as programs_count
                FROM
                    { inputs["search_events"].get_table_name_by_date(task_date_normalized) }
                UNION ALL
                -- goals
                SELECT
                    'reach_goal' AS action,
                    msk_date,
                    client_id,
                    [] as tags,
                    [] as types,
                    [] as queries,
                    [] as program_ids,
                    0 as programs_count
                FROM
                    { inputs["goals"].get_table_name_by_date(task_date_normalized) }
                where not isNull(goal)
                UNION ALL

                -- program views
                SELECT
                    'view_program' AS action,
                    msk_date,
                    client_id,
                    [] as tags,
                    [] as types,
                    [] as queries,
                    program_ids,
                    programs_count
                FROM
                    { inputs["program_views"].get_table_name_by_date(task_date_normalized) }
            ) as s
            JOIN (
                -- user meta
                SELECT
                    msk_date,
                    client_id,
                    first_value(utm_campaign) as utm_campaign,
                    first_value(utm_content) as utm_content,
                    first_value(utm_medium) as utm_medium,
                    first_value(utm_source) as utm_source,

                    first_value(country) as country,
                    first_value(city) as city,
                    first_value(os_family) as os_family,
                    first_value(device_type) as device_type
                FROM
                    { inputs["visits"].get_table_name_by_date(task_date_normalized) }
                GROUP BY
                    msk_date,
                    client_id
            ) AS t
            USING client_id, msk_date
        )
    """)

    db.create_logtype_table(
        outputs["conversion_cube_cumulative"],
        task_date_normalized,
        drop=False
    )

    db.query(f"""
        INSERT INTO 
            conversion.conversion
        SELECT
            *
        FROM {outputs["conversion_cube"].get_table_name_by_date(task_date_normalized)}
    """)

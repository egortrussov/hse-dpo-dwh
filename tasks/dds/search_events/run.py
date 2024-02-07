
from infra.database import Database
from datetime import datetime


db = Database()
db.connect()

def run(client, inputs, outputs, task_date: datetime):
    task_date_normalized = task_date.isoformat()[:10]

    db.create_logtype_table(outputs["search_events"], task_date_normalized)

    db.query(f"""
        INSERT INTO
            { outputs["search_events"].get_table_name_by_date(task_date_normalized) }
        SELECT
            msk_date,
            client_id,
            arrayDistinct(groupArrayArray(search_tags)) as tags,
            arrayDistinct(groupArrayArray(search_types)) as types,
            arrayFilter(
                x -> x != '',
                arrayDistinct(groupArray(search_query))
            ) as queries
        FROM { inputs["visits"].get_table_name_by_date(task_date_normalized) }
        WHERE
            search_tags != [] OR
            search_types != [] OR
            search_query != ''
        GROUP BY
            msk_date,
            client_id
        HAVING
            tags != [] OR
            types != [] OR
            (queries != [] AND queries != [''])
    """)

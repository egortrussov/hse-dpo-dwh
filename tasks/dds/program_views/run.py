
from infra.database import Database
from datetime import datetime


def run(client, inputs, outputs, task_date: datetime):
    task_date_normalized = task_date.isoformat()[:10]

    client.create_logtype_table(outputs["program_views"], task_date_normalized)

    client.query(f"""
        INSERT INTO
            { outputs["program_views"].get_table_name_by_date(task_date_normalized) }
        SELECT
            client_id,
            msk_date,
            arrayDistinct(groupArray(program_id)) as program_ids,
            length(program_ids) AS programs_count
        FROM { inputs["visits"].get_table_name_by_date(task_date_normalized) }
        WHERE
            page_type = 'program_page' AND
            NOT isNull(program_id)
        GROUP BY
            msk_date,
            client_id
        HAVING
            program_ids != []
    """)

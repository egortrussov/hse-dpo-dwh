
from infra.database import Database
from datetime import datetime


def run(client, inputs, outputs, task_date: datetime):
    task_date_normalized = task_date.isoformat()[:10]

    client.create_logtype_table(outputs["hits_enriched"], task_date_normalized, drop=False)

    client.query(f"""
        INSERT INTO
            { outputs["hits_enriched"].get_table_name_by_date(task_date_normalized) }
        SELECT
            *
        FROM
            { inputs["dds_hits"].get_table_name_by_date(task_date_normalized) } AS s
    """)

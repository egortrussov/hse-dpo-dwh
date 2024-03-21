
from infra.database import Database
from datetime import datetime


db = Database()
db.connect()

def run(client, inputs, outputs, task_date: datetime):
    task_date_normalized = task_date.isoformat()[:10]

    db.create_logtype_table(outputs["hits_enriched"], task_date_normalized)

    db.query(f"""
        INSERT INTO
            { outputs["hits_enriched"].get_table_name_by_date(task_date_normalized) }
        SELECT
            *
        FROM
            { inputs["dds_hits"].get_table_name_by_date(task_date_normalized) } AS s
    """)

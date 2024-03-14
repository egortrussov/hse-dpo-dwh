
from infra.database import Database
from datetime import datetime


db = Database()
db.connect()

def run(client, inputs, outputs, task_date: datetime):
    task_date_normalized = task_date.isoformat()[:10]

    db.create_logtype_table(outputs["goals"], task_date_normalized)

    db.query(f"""
        INSERT INTO
            { outputs["goals"].get_table_name_by_date(task_date_normalized) }
        SELECT
            client_id,
            msk_date,
            goal,
            goal_rus,
            program_id
        FROM { inputs["visits"].get_table_name_by_date(task_date_normalized) }
        WHERE
            NOT isNull(goal)
    """)

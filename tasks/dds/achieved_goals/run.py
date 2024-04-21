
from infra.database import Database
from datetime import datetime


def run(client, inputs, outputs, task_date: datetime):
    task_date_normalized = task_date.isoformat()[:10]

    client.create_logtype_table(outputs["goals"], task_date_normalized)

    client.query(f"""
        INSERT INTO
            { outputs["goals"].get_table_name_by_date(task_date_normalized) }
        SELECT
            client_id,
            msk_date,
            goal,
            goal_name,
            visit_param_goal,
            visit_param_goal_rus,
            visit_param_goal_program_id
        FROM { inputs["visits"].get_table_name_by_date(task_date_normalized) }
        WHERE
            NOT isNull(goal)
    """)

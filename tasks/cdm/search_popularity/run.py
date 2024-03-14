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

    db.create_logtype_table(outputs["search_popularity"], task_date_normalized)

    db.query(f"""
        INSERT INTO
            { outputs["first_visits"].get_table_name_by_date(task_date_normalized) }
        SELECT
            msk_date,
            "tags" as search_type,
            ArrayJoin(tags) as search_value,
            0 as count
        FROM
            { inputs["search_events"].get_table_name_by_date(task_date_normalized) }
    """)


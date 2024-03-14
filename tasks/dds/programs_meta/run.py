
from infra.database import Database
from infra.table_container import (
    TableContainer,
)
import json

from datetime import datetime


db = Database()
db.connect()

def run(client, inputs, outputs, task_date: datetime):
    db.create_logtype_table(outputs["programs_meta"])

    meta = json.load(open("static/programs_meta.json"))

    table = TableContainer()
    table.init_from_list_of_dicts(meta)

    table.save_data_to_log(
        db.get_client(),
        outputs["programs_meta"]
    )

    

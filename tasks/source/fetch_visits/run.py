from infra import (
    LogsFetcher,
    save_data_to_log,
)
from datetime import datetime
from .utils import (
    METRIKA_FIELDS,
)

def run(client, inputs, outputs, task_date: datetime):
    task_date_normalized = task_date.isoformat()[:10]
    fetcher = LogsFetcher()

    print("Running task for date " + task_date_normalized)

    fetcher.fetch_logs(
        date_start=task_date_normalized,
        date_end=task_date_normalized,
        fields_list=METRIKA_FIELDS,
        logs_type="visits",
    )

    save_data_to_log(
        client.get_client(),
        log_type=outputs["visits"],
        data=fetcher.get_rows(),
        date=task_date_normalized,
    )

from infra import (
    LogsFetcher,
    save_data_to_log,
)
from infra.table_container import (
    TableContainer,
)
from infra.query_sender import (
    send_select_query,
)
from infra.table_processing import (
    represent_table_as_list_of_dicts,
)
from datetime import datetime
from .utils import (
    get_goals_names,
    get_goals_program_ids,
    parse_goal,
)
from copy import deepcopy

def run(client, inputs, outputs, task_date: datetime):
    task_date_normalized = task_date.isoformat()[:10]
    input_table = inputs["source_visits"].get_table_name_by_date(task_date_normalized)

    table = send_select_query(
        client,
        inputs["source_visits"],
        task_date_normalized,
        fields=None,
        # filters=RAW_HITS_FILTER,
    )

    table.rename_fields(
        visitID="visit_id",
        clientID="client_id",
        watchIDs="watch_ids",
        date="msk_date",
        parsedParamsKey1="parsed_params_key_1",
        parsedParamsKey2="parsed_params_key_2",
        parsedParamsKey3="parsed_params_key_3",
        parsedParamsKey4="parsed_params_key_4",
        parsedParamsKey5="parsed_params_key_5",
        goalsID="goals_id",
        ipAddress="ip",
        regionCountry="country",
        regionCity="city",
        firstTrafficSource="first_traffic_source",
        lastTrafficSource="last_traffic_source",
        lastsignUTMSource="utm_source",
        lastsignUTMCampaign="utm_campaign",
    )

    table.map_rows(parse_row, is_multiple_output=True)

    table.save_data_to_log(
        client,
        outputs["parsed_visits"],
        task_date_normalized,
    )


def parse_row(row):
    if row["parsed_params_key_3"] == "[]":
        row["goal"] = None
        row["goal_rus"] = None
        row["program_id"] = None
        return [row]
    goals_names = get_goals_names(row["parsed_params_key_3"])
    goals_program_ids = get_goals_program_ids(row["parsed_params_key_3"])
    
    result_rows = []
    
    for (goal_name, program_id) in zip(goals_names, goals_program_ids):
        goal_rus = goal_name
        goal_parsed = parse_goal(goal_name)
        result_rows.append(deepcopy(row))
        
        result_rows[-1]["goal"] = goal_parsed
        result_rows[-1]["goal_rus"] = goal_name
        result_rows[-1]["program_id"] = program_id

    return result_rows
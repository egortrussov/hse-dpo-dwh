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
    get_goal_name,
)
from copy import deepcopy
from infra.database import Database


db = Database()
db.connect()

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
    print("------")
    table.map_rows(parse_row_goals, is_multiple_output=True)

    table.save_data_to_log(
        client,
        outputs["parsed_visits"],
        task_date_normalized,
    )
    
    db.create_logtype_table(
        outputs["visits_cumulative"],
        task_date_normalized,
        drop=False
    )

    db.query(f"""
        INSERT INTO 
            conversion.visits
        SELECT
            *
        FROM {outputs["parsed_visits"].get_table_name_by_date(task_date_normalized)}
    """)


def parse_row(row):
    if row["parsed_params_key_3"] == "[]":
        row["visit_param_goal"] = None
        row["visit_param_goal_rus"] = None
        row["visit_param_goal_program_id"] = None
        return [row]
    goals_names = get_goals_names(row["parsed_params_key_3"])
    goals_program_ids = get_goals_program_ids(row["parsed_params_key_3"])
    
    result_rows = []
    
    for (goal_name, program_id) in zip(goals_names, goals_program_ids):
        goal_rus = goal_name
        goal_parsed = parse_goal(goal_name)
        result_rows.append(deepcopy(row))
        
        result_rows[-1]["visit_param_goal"] = goal_parsed
        result_rows[-1]["visit_param_goal_rus"] = goal_name
        result_rows[-1]["visit_param_goal_program_id"] = program_id

    return result_rows


def parse_row_goals(row):
    if row["goals_id"] == "[]":
        row["goal"] = None
        row["goal_name"] = None
        return [row]
    goals_id_list = row["goals_id"][1:-1].split(",")
    result_rows = []
    
    for goal_id in goals_id_list:
        result_rows.append(deepcopy(row))
        result_rows[-1]["goal"] = goal_id
        result_rows[-1]["goal_name"] = get_goal_name(goal_id)

    return result_rows
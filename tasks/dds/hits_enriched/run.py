
from infra.database import Database
from datetime import datetime


def run(client, inputs, outputs, task_date: datetime):
    task_date_normalized = task_date.isoformat()[:10]

    client.create_logtype_table(outputs["hits_enriched"], task_date_normalized)

    client.query(f"""
        INSERT INTO
            { outputs["hits_enriched"].get_table_name_by_date(task_date_normalized) }
        SELECT
            s.*,
            t.program_title as program_title,
            t.program_type as program_type,
            t.program_org_unit_id as program_org_unit_id,
            t.program_org_unit_title as program_org_unit_title
        FROM
            { inputs["ods_hits"].get_table_name_by_date(task_date_normalized) } AS s
        LEFT JOIN (
            SELECT
                id as program_id,
                title as program_title,
                type as program_type,
                org_unit_id as program_org_unit_id,
                org_unit_title as program_org_unit_title
            FROM
                { inputs["programs_meta"].get_table_name_by_date(task_date_normalized) } AS t
        ) as t
        ON
            s.program_id = t.program_id
    """)

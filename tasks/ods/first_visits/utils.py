FIELDS = [
    "ym:pv:clientID",
    "ym:pv:date",
    "ym:pv:dateTime",
]


def get_first_visits_query(table_path):
    return f"""
        INSERT INTO
            {table_path[:-1]}_temp`
        SELECT
            client_id,
            MIN(msk_date) as msk_date,
            MIN(datetime) as datetime
        FROM
            {table_path}
        GROUP BY
            client_id
    """

def get_first_visits_query1(table_path):
    return f"""
        INSERT INTO
            {table_path}
        SELECT
            *
        FROM
            {table_path[:-1]}_temp`
        ORDER BY
            msk_date
    """
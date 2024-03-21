import clickhouse_connect
from infra.log_types import LogTypeBase


class Database:

    def __init__(self):
        self.client = None


    def connect(self):
        self.client = clickhouse_connect.get_client(host='172.18.0.4')
        # self.client = clickhouse_connect.get_client(host='localhost')
    
    

    def get_client(self):
        return self.client
    

    def create_logtype_table(
            self,
            logtype: LogTypeBase,
            date_str = None,
            drop  = True
    ):
        table_path = logtype.get_table_name_by_date(date_str)
        
        self.client.query(
            f"CREATE DATABASE IF NOT EXISTS {logtype.get_database()}"
        )

        if drop:
            self.drop_table(logtype, date_str)

        create_table_query = f"""
            CREATE TABLE IF NOT EXISTS
            { table_path }
            (
                { logtype.get_fields_list_with_types() }
            )
            ENGINE { logtype.get_engine() }
        """

        self.client.command(create_table_query)
    

    def query(self, query: str):
        self.client.command(query)

    
    def drop_table(self, logtype: LogTypeBase, date_str: str = None):
        drop_table_query = f"""
            DROP TABLE IF EXISTS
            { logtype.get_table_name_by_date(date_str) }
        """
        self.client.command(drop_table_query)

    # def drop_table(self, path: str):
    #     drop_table_query = f"""
    #         DROP TABLE IF EXISTS
    #         { path }
    #     """
    #     self.client.command(drop_table_query)


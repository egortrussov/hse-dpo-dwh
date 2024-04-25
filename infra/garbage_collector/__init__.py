from infra.logtypes import (
    LogTypeWithTTL,
)
from infra.database import (
    Database,
)
import datetime as dt

class GarbageCollector:
    
    def __init__(self, database, log_types: list[LogTypeWithTTL]):
        """
        self.log_types - list of logtypes to watch for garbage collection
        """
        self.database = database
        self.log_types = log_types
        
        self.__assert_logtypes()
        
    
    def collect(self):
        for logtype in self.log_types:
            tables = self.get_logtype_tables(logtype)
            limit_date = dt.datetime.now() - dt.timedelta(logtype.get_ttl())
            limit_date_str = limit_date.isoformat()[:10]
            
            for table in tables:
                if table == logtype.get_name():
                    continue     
                

                if table >= logtype.get_name() + "_" + limit_date_str:
                    continue
                

                self.database.drop_table_by_name(
                    logtype.get_database(),
                    table,
                )
    
    def get_logtype_tables(self, logtype: LogTypeWithTTL):
        return str(self.database.query(f"""
            SHOW TABLES
            FROM { logtype.get_database() }
            LIKE '{ logtype.get_name() }%'
        """)).split("\n")
    
    
    def __assert_logtypes(self):
        for logtype in self.log_types:
            if not isinstance(logtype, LogTypeWithTTL):
                raise "Garbage collector only works with ttl-ed logtypes: " + logtype.__name__
    
        
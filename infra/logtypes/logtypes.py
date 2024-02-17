from .logtype_base import (
    LogTypeBase,
)
from infra.database import (
    Field,
)


class PermanentLogType(LogTypeBase):

    def __init__(
            self,
            database,
            name,
            fields_list: list[Field],
            engine = "Log",
    ):
        super().__init__(database, name, fields_list, engine)


class StaticLogType(LogTypeBase):

    def __init__(
            self,
            database,
            name,
            fields_list: list[Field],
            engine = "Log",
    ):
        super().__init__(database, name, fields_list, engine)
    

    def get_table_name_by_date(self, date_str = None):
        return self.database + ".`" + self.name + "`"



class LogTypeWithTTL(LogTypeBase):

    def __init__(
            self,
            database,
            name,
            fields_list: list[Field],
            engine = "Log",
            ttl = None,
    ):
        super().__init__(database, name, fields_list, engine)
        self.ttl = ttl


    def get_ttl(self):
        return self.ttl

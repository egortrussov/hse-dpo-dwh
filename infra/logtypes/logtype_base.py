from infra.database import (
    Field,
)


class LogTypeBase:

    def __init__(
            self,
            database,
            name,
            fields_list: list[Field],
            engine = "Log",
    ):
        self.database = database
        self.name = name
        self.fields = fields_list
        self.engine = engine


    def get_fields_list_with_types(self):
        result_list = []
        
        for field_data in self.fields:
            result_list.append(field_data.name + " " + field_data.ch_type)

        return ",\n".join(result_list)


    def get_table_name_by_date(self, date_str):
        return self.database + ".`" + self.name + "_" + date_str + "`"


    def get_fields(self):
        fields_list = []
        for field in self.fields:
            fields_list.append(field.name)
        return fields_list
    

    def get_types(self):
        types_list = []
        for field in self.fields:
            types_list.append(field.py_type)
        return types_list


    def get_engine(self):
        return self.engine

    def get_database(self):
        return self.database
    

    def get_ttl(self):
        return None

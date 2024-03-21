class LogTypeBase:

    def __init__(self, database, name, fields, fields_types, engine = 'Log'):
        self.database = database
        self.name = name
        self.fields = fields
        self.fields_types = fields_types
        self.engine = engine
        

    def get_fields_list_with_types(self):
        result_list = []
        assert(len(self.fields) == len(self.fields_types))
        for (field, type) in zip(self.fields, self.fields_types):
            result_list.append(field + " " + type)
        return ",\n".join(result_list)


    def get_table_name_by_date(self, date_str):
        return self.database + ".`" + self.name + "_" + date_str + "`"


    def get_fields(self):
        return self.fields
    

    def get_engine(self):
        return self.engine

    def get_database(self):
        return self.database
    

    def get_ttl(self):
        return None


class PermanentLogType(LogTypeBase):

    def __init__(self, database, name, fields, fields_types):
        super().__init__(database, name, fields, fields_types)


class StaticLogType(LogTypeBase):

    def __init__(self, database, name, fields, fields_types):
        super().__init__(database, name, fields, fields_types)
    

    def get_table_name_by_date(self, date_str = None):
        return self.database + ".`" + self.name + "`"



class LogTypeWithTTL(LogTypeBase):

    def __init__(self, database, name, fields, fields_types, engine, ttl):
        super().__init__(database, name, fields, fields_types, engine)
        self.ttl = ttl


    def get_ttl(self):
        return self.ttl

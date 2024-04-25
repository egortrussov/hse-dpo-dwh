from infra.logtypes.logtype_base import LogTypeBase
from .table_saver import save_data_to_log


class TableContainer:

    def __init__(self, fields = [], rows = []):
        self.fields = list(fields)
        self.rows = list(rows)

    
    def init_from_list_of_dicts(self, rows):
        self.fields = []
        self.rows = []
        for field in rows[0].keys():
            self.fields.append(field)
        for row in rows:
            self.rows.append([])
            for field in self.fields:
                self.rows[-1].append(row[field])
        print(len(self.rows))


    def rename_fields(self, **fields_to_rename):
        for field, new_field_name in fields_to_rename.items():
            for i in range(len(self.fields)):
                if self.fields[i] == field:
                    self.fields[i] = new_field_name


    def represent_as_list_of_dicts(self):
        result = []

        for row in self.rows:
            result.append({})
            for field, value in zip(self.fields, row):
                result[-1][field] = value

        return result
    

    def map_rows(self, mapper_function, is_multiple_output=False):
        table_dict = self.represent_as_list_of_dicts()
        table_dict_mapped = []
    
        if not is_multiple_output:
            table_dict_mapped = list(map(
                mapper_function,
                table_dict
            ))
        else:
            for row in table_dict:
                for res in mapper_function(row):
                    table_dict_mapped.append(res)

        self.__convert_list_of_dicts_to_table(table_dict_mapped)
    

    def save_data_to_log(
            self,
            client,
            log_type: LogTypeBase,
            date = None,
    ):
        save_data_to_log(
            client,
            log_type,
            self.__prepare_rows_for_schema(log_type.get_fields(), log_type.get_types()),
            date
        )


    def __prepare_rows_for_schema(self, schema, types=None):
        rows_dict_list = self.represent_as_list_of_dicts()
        rows_prepared = []
        print(schema)
        print(self.fields)
        for row in self.rows:
            rows_prepared.append([])
            for (schema_field, field_type) in zip(schema, types):
                if schema_field not in self.fields:
                    raise Exception(f"Field {schema_field} not found in table representation")
                if len(row) <= self.fields.index(schema_field):
                    continue
                # print(row[self.fields.index(schema_field)])
                if row[self.fields.index(schema_field)] is None:
                    rows_prepared[-1].append(row[self.fields.index(schema_field)])
                else:
                    rows_prepared[-1].append(field_type(row[self.fields.index(schema_field)]))
        print(len(rows_prepared))
        return rows_prepared


    def __convert_list_of_dicts_to_table(self, table_dict):
        if len(table_dict) == 0:
            self.fields = self.rows = []
            return
        self.fields = list(table_dict[0].keys())
        self.rows = []
        for row in table_dict:
            self.rows.append([None] * len(self.fields))
            for field, value in row.items():
                self.rows[-1][self.fields.index(field)] = value

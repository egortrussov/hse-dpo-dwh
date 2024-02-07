from infra.log_types import LogTypeBase
from infra import table_saver


class TableContainer:

    def __init__(self, fields, rows):
        self.fields = list(fields)
        self.rows = list(rows)


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
    

    def map_rows(self, mapper_function):
        table_dict = self.represent_as_list_of_dicts()

        table_dict_mapped = list(map(
            mapper_function,
            table_dict
        ))

        self.__convert_list_of_dicts_to_table(table_dict_mapped)
    

    def save_data_to_log(
            self,
            client,
            log_type: LogTypeBase,
            date,
    ):
        table_saver.save_data_to_log(
            client,
            log_type,
            self.__prepare_rows_for_schema(log_type.get_fields()),
            date
        )


    def __prepare_rows_for_schema(self, schema):
        rows_dict_list = self.represent_as_list_of_dicts()
        rows_prepared = []
        for row in self.rows:
            rows_prepared.append([])
            for schema_field in schema:
                if schema_field not in self.fields:
                    raise Exception(f"Field {schema_field} not found in table representation")
                if len(row) <= self.fields.index(schema_field):
                    continue
                if row[self.fields.index(schema_field)] is None:
                    print(schema_field)
                rows_prepared[-1].append(row[self.fields.index(schema_field)])
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

from .log_types import LogTypeBase


def represent_table_as_list_of_dicts(
        fields,
        rows,
):
    result = []

    for row in rows:
        result.append({})
        for field, value in zip(fields, row):
            result[-1][field] = value

    return result
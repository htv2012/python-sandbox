from prettytable import PrettyTable, TableStyle


def create_table(field_names: list[str], alignment: str, rows: list):
    table = PrettyTable(field_names=field_names)
    table.set_style(TableStyle.DOUBLE_BORDER)
    for name, align in zip(field_names, alignment):
        table.align[name] = align
    table.add_rows(rows)
    return table

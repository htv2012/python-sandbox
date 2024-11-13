from prettytable import PrettyTable

table = PrettyTable(field_names=["UID", "alias", "shell"])
for field_name in table.align:
    table.align[field_name] = "l"

table.add_row([501, "peter", "bash"])
table.add_row([502, "paul", "tcsh"])
table.add_row([503, "mary", "zsh"])
print(table)

# OUTPUT
# +-----+-------+-------+
# | UID | alias | shell |
# +-----+-------+-------+
# | 501 | peter |  bash |
# | 502 | paul  |  tcsh |
# | 503 | mary  |  zsh  |
# +-----+-------+-------+

from decimal import Decimal

from prettytable import PrettyTable, TableStyle


def main():
    table = PrettyTable()
    table.set_style(TableStyle.SINGLE_BORDER)
    table.title = "LinkedIn Plans Comparison"
    table.field_names = ["Month", "Monthly", "Quarterly", "Anual"]
    table.align = "r"

    monthly_rate = Decimal("29.99")
    quarterly_rate = Decimal("67.48")
    anual_rate = Decimal("179.91")

    for month in range(1, 13):
        a_cost = anual_rate
        m_cost = month * monthly_rate
        q_count, rem = divmod(month, 3)
        if rem > 0:
            q_count += 1

        q_cost = q_count * quarterly_rate
        table.add_row([month, m_cost, q_cost, a_cost])

    print(table)


if __name__ == "__main__":
    main()

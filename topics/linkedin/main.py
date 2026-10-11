from decimal import Decimal


def main():
    print()
    print("LinkedIn Plans Comparison".center(48))
    print("=========================".center(48))
    print()

    for heading in ["Month", "Monthly", "Quarterly", "Anual"]:
        print(f"{heading:>12}", end="")
    print()

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

        print(f"{month:>12}", end="")
        print(f"{m_cost:>12.2f}", end="")
        print(f"{q_cost:>12.2f}", end="")
        print(f"{a_cost:>12.2f}", end="")
        print()


if __name__ == "__main__":
    main()


import click

from clicklib import EndConditionParamType


@click.command
@click.argument(
    "end_condition",
    type=EndConditionParamType(),
    metavar="END_CONDITION",
    required=False,
)
def main(end_condition):
    print(f"{end_condition = }")


if __name__ == "__main__":
    main()

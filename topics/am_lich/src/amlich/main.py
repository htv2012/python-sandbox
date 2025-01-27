import argparse
import importlib.metadata


def d2a(year: int):
    can_lookup = {
        1: "Giáp",
        2: "Ấ́t",
        3: "Bính",
        4: "Đinh",
        5: "Mậu",
        6: "Kỷ",
        7: "Canh",
        8: "Tân",
        9: "Nhâm",
        0: "Quý",
    }

    chi_lookup = {
        1: "Tý",
        2: "Sửu",
        3: "Dần",
        4: "Mão",
        5: "Thìn",
        6: "Tỵ",
        7: "Ngọ",
        8: "Mùi",
        9: "Thân",
        10: "Dậu",
        11: "Tuất",
        0: "Hợi",
    }

    can = (year - 3) % 10
    chi = (year - 3) % 12
    out = f"{can_lookup[can]} {chi_lookup[chi]}"
    return out


def main() -> None:
    parser = argparse.ArgumentParser(prog="amlich")
    parser.add_argument("-d", "--d2a", dest="year", type=int)
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s " + importlib.metadata.version("amlich"),
    )
    options = parser.parse_args()

    if options.year:
        ayear = d2a(options.year)
        print(ayear)


if __name__ == "__main__":
    main()

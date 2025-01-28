def dl_to_al(year: int):
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


def al_to_dl(year: str, start_year: int, end_year: int):
    pass

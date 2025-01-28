def get_am_lich(year: int):
    can_lookup = {
        1: "Giap",
        2: "At",
        3: "Binh",
        4: "Dinh",
        5: "Mau",
        6: "Ky",
        7: "Canh",
        8: "Tan",
        9: "Nham",
        0: "Quy",
    }

    chi_lookup = {
        1: "Ti",
        2: "Suu",
        3: "Dan",
        4: "Mao",
        5: "Thin",
        6: "Ty",
        7: "Ngo",
        8: "Mui",
        9: "Than",
        10: "Dau",
        11: "Tuat",
        0: "Hoi",
    }

    can = (year - 3) % 10
    chi = (year - 3) % 12
    out = f"{can_lookup[can]} {chi_lookup[chi]}"
    return out


def to_vietnamese(text: str):
    can_lookup = {
        "Giap": "Giáp",
        "At": "Ất",
        "Binh": "Bính",
        "Dinh": "Đinh",
        "Mau": "Mậu",
        "Ky": "Kỷ",
        "Canh": "Canh",
        "Tan": "Tân",
        "Nham": "Nhâm",
        "Quy": "Quý",
    }
    chi_lookup = {
        "Ti": "Tí",
        "Suu": "Sửu",
        "Dan": "Dần",
        "Mao": "Mão",
        "Thin": "Thìn",
        "Ty": "Tỵ",
        "Ngo": "Ngọ",
        "Mui": "Mùi",
        "Than": "Thân",
        "Dau": "Dậu",
        "Tuat": "Tuất",
        "Hoi": "Họi",
    }

    for table in [can_lookup, chi_lookup]:
        for old, new in table.items():
            text = text.replace(old, new)
    return text

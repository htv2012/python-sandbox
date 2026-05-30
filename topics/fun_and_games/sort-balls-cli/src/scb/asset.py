import enum


class Asset(enum.StrEnum):
    EMPTY = "◼️"
    CHECKED = "✅"
    POP = "⬆"
    PUSH = "⬇"
    # ⬆ ⬇ ↑ ↓

    @classmethod
    def balls(cls):
        return ["🔴", "🟠", "🟡", "🟢", "🔵", "🟣", "🟤"]

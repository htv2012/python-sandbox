import re


class PastedSheetsTracker(object):
    def __init__(self, sheets_before_paste):
        self.sheets = set(sheets_before_paste)

    def get_pasted_sheet_name(self, original_sheet_name):
        if original_sheet_name not in self.sheets:
            msg = "Sheet not in list: {}".format(original_sheet_name)
            raise ValueError(msg)

        pattern = re.compile(r"(.*?) *\((\d+)\)")
        match = re.match(pattern, original_sheet_name)
        if match:
            base_name, serial = match.groups()
            serial = int(serial)
        else:
            base_name, serial = original_sheet_name, 1

        while True:
            serial += 1
            new_name = "{} ({})".format(base_name, serial)
            if new_name not in self.sheets:
                self.sheets.add(new_name)
                return new_name


if __name__ == "__main__":
    current_sheets = ["Worksheet A", "Worksheet A (2)", "Dashboard 1"]
    tracker = PastedSheetsTracker(current_sheets)

    sheet = "Dashboard 1"
    print(sheet, "==>", tracker.get_pasted_sheet_name(sheet))

    sheet = "Worksheet A (2)"
    print(sheet, "==>", tracker.get_pasted_sheet_name(sheet))

    sheet = "Worksheet A"
    print(sheet, "==>", tracker.get_pasted_sheet_name(sheet))

    print("\nSheets after pasted:\n-", "\n- ".join(sorted(tracker.sheets)))

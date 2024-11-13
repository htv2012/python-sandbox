#!/usr/bin/env python3
import re

import schematics


class PhoneNumber(schematics.types.StringType):
    def validate_chars(self, value):
        """Charset must be 0-9 and dash."""
        if not all(c in "0123456789-" for c in value):
            raise schematics.exceptions.ValidationError(
                "Chars must be digits and dash."
            )

    def validate_format(self, value):
        if not re.match(r"\d{3}-\d{3}-\d{4}", value):
            raise schematics.exceptions.ValidationError(
                "Incorrect format, expect xxx-xxx-xxxx."
            )


class PhoneEntry(schematics.models.Model):
    name = schematics.types.StringType(required=True)
    mobile = PhoneNumber(required=True)


ph = PhoneEntry({"name": "John", "mobile": "(512)3467"})
# ph.validate()
try:
    ph.validate()
except schematics.exceptions.DataError as error:
    for field_name, faults in error.to_primitive().items():
        print(f"{field_name}:")
        for fault in faults:
            print(f"- {fault}")

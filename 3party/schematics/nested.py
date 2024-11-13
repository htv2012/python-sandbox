#!/usr/bin/env python3
import json
import string

import schematics


def validate_no_space(value):
    """fields must not have spaces."""
    if " " in value:
        raise schematics.exceptions.ValidationError("There must not be spaces in value")


class UserMetadata(schematics.Model):
    """Model a user metadata."""
    name = schematics.types.StringType(required=True)
    display_name = schematics.types.StringType(serialized_name="displayName")
    description = schematics.types.StringType()

    # In order to validate a field, say field X, create a method called validate_X
    # @staticmethod
    def validate_name(self, json_obj, name):
        """
        Validate name.

        :param json_obj: The original JSON object used to create the instance
        :param name: The name to validate
        :raise schematics.exceptions.ValidationError: If validation failed
        """
        valid_chars_set = string.ascii_letters + string.digits + "_"
        if not all(c in valid_chars_set for c in name):
            raise schematics.exceptions.ValidationError(
                f"Expect only letters, digits and underscore, but got {name!r}"
            )


class UserDef(schematics.Model):
    """Model a user definition."""
    first_name = schematics.types.StringType(
        serialized_name="firstName", validators=[validate_no_space]
    )
    last_name = schematics.types.StringType(
        serialized_name="lastName", validators=[validate_no_space]
    )
    email = schematics.types.EmailType()


class User(schematics.Model):
    """Model a user object with nested data."""
    metadata = schematics.types.ModelType(UserMetadata)
    user_def = schematics.types.ModelType(UserDef, serialized_name="userDef")


def verify(json_obj):
    """Drive the validation and report."""
    user = User(json_obj)

    print("-" * 72)
    print("Validating:")
    print(json.dumps(json_obj, indent=4))

    try:
        user.validate()
    except schematics.exceptions.DataError as error:
        print(f"Error: {error}")
    else:
        print("OK")


# Should be OK
verify(
    {
        "metadata": {
            "name": "Johan",
            "displayName": "Johan Anderson",
            "description": "System admin",
        },
        "userDef": {
            "firstName": "Johan",
            "lastName": "Anderson",
            "email": "johan@comix.com",
        },
    }
)

# Email and name errors
verify(
    {
        "metadata": {
            "name": "Johan",
            "displayName": "Johan Anderson",
            "description": "System admin",
        },
        "userDef": {
            "firstName": "Johan Ken",
            "lastName": "Anderson",
            "email": "johan",
        },
    }
)

# name is missing
verify(
    {
        "metadata": {
            "displayName": "Johan Anderson",
            "description": "System admin",
        },
        "userDef": {
            "firstName": "Johan",
            "lastName": "Anderson",
            "email": "johan@comix.com",
        },
    }
)

# Bad name
verify(
    {
        "metadata": {
            "name": "johnny-five",
            "displayName": "Johan Anderson",
            "description": "System admin",
        },
        "userDef": {
            "firstName": "Johan",
            "lastName": "Anderson",
            "email": "johan@comix.com",
        },
    }
)

#!/usr/bin/env python3
from enum import Enum


class LicenseType(str, Enum):
    NONE = "NONE"
    PAID = "PAID"


def test_paid():
    assert LicenseType.PAID == "PAID"


def test_none():
    assert LicenseType.NONE == "NONE"

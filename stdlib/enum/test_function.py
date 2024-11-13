#!/usr/bin/env python
import enum

Mood = enum.Enum("Mood", [("happy", 1), ("sad", 2)])


def test_name():
    assert Mood.happy.name == "happy"


def test_value():
    assert Mood.happy.value == 1


def test_init():
    assert Mood(1) == Mood.happy

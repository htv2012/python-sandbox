#!/usr/bin/env python3
"""Nested model."""
from typing import Optional, List

from pydantic import BaseModel

class Metadata(BaseModel):
    name: Optional[str]
    tags: Optional[List[str]]


m_empty = Metadata()
m_name = Metadata(name="env1")
m_full = Metadata(name="env2", tags=["foo", "bar"])

print(f"{m_empty=}")
print(f"{m_name=}")
print(f"{m_full=}")

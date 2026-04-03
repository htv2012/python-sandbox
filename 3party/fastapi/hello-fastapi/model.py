from typing import Optional

from pydantic import BaseModel

__all__ = ["UserCreate"]


class UserCreate(BaseModel):
    alias: str
    shell: str
    is_admin: bool


class UserUpdate(BaseModel):
    shell: Optional[str] = None
    is_admin: Optional[bool] = None

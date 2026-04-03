from pydantic import BaseModel

__all__ = ["UserCreate"]


class UserCreate(BaseModel):
    alias: str
    shell: str
    is_admin: bool

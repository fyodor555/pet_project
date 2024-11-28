from typing import Optional
from pydantic import BaseModel


class SPersonAdd(BaseModel):
    name: str
    surname: str
    post: Optional[str] = None
    age: Optional[int] = None
    discription: Optional[str] = None


class SPerson(SPersonAdd):
    id: int


class SPersonId(BaseModel):
    ok: bool = True
    person_id: int
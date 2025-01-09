from typing import Optional
from pydantic import BaseModel


class STaskAdd(BaseModel):
    title: str
    discription: Optional[str] = None


class STaskGet(STaskAdd):
    id: int


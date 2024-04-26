from pydantic import BaseModel
from typing import Optional


class Person(BaseModel):
    name: str
    age: int
    bio: Optional[str] = None
    id: Optional[int] = None


class Location(BaseModel):
    id: Optional[int] = None
    name: str
    state: str
    city: Optional[str] = None
    county: str
    street_address: Optional[str] = None
    country: str
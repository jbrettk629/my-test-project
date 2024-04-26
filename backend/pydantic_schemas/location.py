from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class LocationBase(BaseModel):
    name: str
    state: str
    city: Optional[str] = None
    county: str
    street_address: Optional[str] = None
    country: str

class LocationCreate(LocationBase):
    ...

class Location(LocationBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
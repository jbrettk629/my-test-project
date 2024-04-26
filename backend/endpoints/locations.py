import fastapi
from typing import List
from cruds.locations import get_location, get_locations, create_location
from db.connections import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from pydantic_schemas.location import Location, LocationCreate


router = fastapi.APIRouter()



@router.get("/locations", response_model=List[Location])
async def read_locations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_locations(db, skip, limit)


@router.post("/create_location")
async def insert_location(location: LocationCreate, db: Session = Depends(get_db)):
    create_location(db, location)
    return "Success"


@router.get("/locations/{id}")
async def read_location(id: int, db: Session = Depends(get_db)):
    return get_location(db=db, location_id=id)
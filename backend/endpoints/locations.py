import fastapi
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from cruds.locations import get_location, get_locations, create_location
from db.connections import get_async_db
from fastapi import Depends, HTTPException
from pydantic_schemas.location import Location, LocationCreate


router = fastapi.APIRouter()



@router.get("/locations", response_model=List[Location])
async def read_locations(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_async_db)):
    return await get_locations(db, skip, limit)


@router.post("/create_location")
async def insert_location(location: LocationCreate, db: AsyncSession = Depends(get_async_db)):
    await create_location(db, location)
    return "Success"


@router.get("/locations/{id}")
async def read_location(id: int, db: AsyncSession = Depends(get_async_db)):
    return await get_location(db=db, location_id=id)
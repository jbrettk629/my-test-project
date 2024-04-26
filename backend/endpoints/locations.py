import fastapi
from typing import List
from models.models import Location
from db.temp_db import DB, create_location

router = fastapi.APIRouter()


@router.get("/locations", response_model=List[Location])
async def read_root():
    return DB["locations"]


@router.post("/create_location")
async def insert_location(location: Location):
    create_location(location)
    return "Success"


@router.get("/locations/{id}")
async def get_location(id: int = fastapi.Path(..., description="The id of the location to retrieve")):
    for location in DB["locations"]:
        if location.id == id:
            return location
    return "No Location Found"
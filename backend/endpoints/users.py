import fastapi
from typing import List
from models.models import Person
from db.temp_db import DB, create_person

router = fastapi.APIRouter()


@router.get("/users", response_model=List[Person])
async def read_root():
    return DB["users"]


@router.post("/create_user")
async def insert_user(user: Person):
    create_person(user.name, user.age)
    return "Success"


@router.get("/users/{id}")
async def get_user(id: int = fastapi.Path(..., description="The id of the user to retrieve")):
    for person in DB:
        if person.id == id:
            return person
    return "No User Found"
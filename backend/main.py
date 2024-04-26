from typing import List, Optional

from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI(
    title="Bretts FastAPI Project",
    description="Application for learning cool shit",
    version="0.0.1",
    contact={
        "name": "J. Brett Kalbacher",
        "email": "jbrettk@gmail.com"
    },
    license_info={"name": "Open Source"}
)

class Person(BaseModel):
    name: str
    age: int
    bio: Optional[str] = None
    id: Optional[int] = None


DB: List[Person] = [
    Person(id=1, name="Brett", age=34, bio=None),
    Person(id=2, name="Kelsey", age=33, bio=None),
    Person(id=3, name="Peyton", age=28, bio=None)
]

def create_person(p_name, p_age):
    next_id = DB[-1].id + 1
    DB.append(Person(id=next_id, name=p_name, age=p_age, bio=None))


@app.get("/users", response_model=List[Person])
async def read_root():
    return DB


@app.post("/create_user")
async def insert_user(user: Person):
    create_person(user.name, user.age)
    return "Success"


@app.get("/users/{id}")
async def get_user(id: int = Path(..., description="The id of the user to retrieve")):
    for person in DB:
        if person.id == id:
            return person
    return "No User Found"





from typing import List
from models.models import Person, Location

DB = {
    "users": [
        Person(id=1, name="Brett", age=34, bio=None),
        Person(id=2, name="Kelsey", age=33, bio=None),
        Person(id=3, name="Peyton", age=28, bio=None)
    ],
    "locations": [
        Location(
            id=1,
            name="Brett's House",
            city="Bend",
            state="Oregon",
            street_address="1982 NE Red Rock Ln.",
            country="United States",
            county="Deschutes County"
            ),
    ]

}

def create_person(user: Person):
    next_id = DB["users"][-1].id + 1
    DB["users"].append(Person(id=next_id, name=user.name, age=user.age, bio=user.bio))


def create_location(location: Location):
    next_id = DB["locations"][-1].id + 1
    DB["locations"].append(
        Location(
            id=next_id,
            name=location.name,
            state=location.state,
            country=location.country,
            city=location.city,
            street_address=location.street_address,
            county=location.county
            )
        )
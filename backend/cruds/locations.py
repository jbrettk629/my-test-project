from sqlalchemy.orm import Session

from db.models.locations import Location
from pydantic_schemas.location import LocationCreate

def get_location(db: Session, location_id: int):
    return db.query(Location).filter(Location.id == location_id).first()

def get_locations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Location).offset(skip).limit(limit).all()

def create_location(db: Session, l: LocationCreate):
    insert = Location(
        name=l.name,
        city=l.city,
        state=l.state,
        street_address=l.street_address,
        county=l.county,
        country=l.country
        )
    db.add(insert)
    db.commit()
    db.refresh(insert)
    return insert
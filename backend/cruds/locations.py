from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError

from db.models.locations import Location
from pydantic_schemas.location import LocationCreate

async def get_location(db: AsyncSession, location_id: int):
    query = select(Location).where(Location.id == location_id)
    result = await db.execute(query)
    return result.scalar_one_or_none()

async def get_locations(db: AsyncSession, skip: int = 0, limit: int = 100):
    query = select(Location)
    result = await db.execute(query)
    return result.scalars()

async def create_location(db: AsyncSession, l: LocationCreate):
    insert = Location(
        name=l.name,
        city=l.city,
        state=l.state,
        street_address=l.street_address,
        county=l.county,
        country=l.country
        )
    db.add(insert)
    await db.commit()
    db.refresh(insert)
    return insert
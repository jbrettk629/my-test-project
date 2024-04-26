from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError

from db.models.users import User
from pydantic_schemas.user import UserCreate

async def get_user(db: AsyncSession, user_id: int):
    query = select(User).where(User.id == user_id)
    result = await db.execute(query)
    return result.scalar_one_or_none()

async def get_users(db: AsyncSession, skip: int = 0, limit: int = 100):
    query = select(User)
    result = await db.execute(query)
    return result.scalars()


async def create_user(db: AsyncSession, user: UserCreate):
    insert = User(name=user.name, age=user.age, bio=user.bio, address=user.address)
    db.add(insert)
    await db.commit()
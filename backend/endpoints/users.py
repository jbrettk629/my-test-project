import fastapi
from typing import List
from cruds.users import get_user, get_users, create_user
from db.connections import get_db, get_async_db
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException
from pydantic_schemas.user import User, UserCreate

router = fastapi.APIRouter()


@router.get("/users", response_model=List[User])
async def read_users(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_async_db)):
    result = await get_users(db, skip=skip, limit=limit)
    return result


@router.post("/create_user")
async def insert_user(user: UserCreate, db: Session = Depends(get_async_db)):
    await create_user(db, user)
    return "Success"



@router.get("/users/{id}")
async def reed_user(id: int, db: AsyncSession = Depends(get_async_db)):
    return await get_user(db, id)

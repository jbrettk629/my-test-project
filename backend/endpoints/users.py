import fastapi
from typing import List
from cruds.users import get_user, get_users, create_user
from db.connections import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from pydantic_schemas.user import User, UserCreate

router = fastapi.APIRouter()


@router.get("/users", response_model=List[User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_users(db, skip=skip, limit=limit)


@router.post("/create_user")
async def insert_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


@router.get("/users/{id}")
async def reed_user(id: int, db: Session = Depends(get_db)):
    return get_user(db, id)
from sqlalchemy.orm import Session

from db.models.users import User
from pydantic_schemas.user import UserCreate

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def get_users_by_address(db: Session, location_id: int):
    return db.query(User).filter(User.address == location_id).all()


def create_user(db: Session, user: UserCreate):
    insert = User(name=user.name, age=user.age, bio=user.bio, address=user.address)
    db.add(insert)
    db.commit()
    db.refresh(insert)
    return user



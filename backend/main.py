from fastapi import FastAPI

from endpoints import users, locations
from db.connections import engine
from db.models import users, locations
from endpoints.users import router as users_router
from endpoints.locations import router as locations_router

users.Base.metadata.create_all(bind=engine)
locations.Base.metadata.create_all(bind=engine)

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

app.include_router(users_router)
app.include_router(locations_router)





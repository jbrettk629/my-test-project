from fastapi import FastAPI, Path

from endpoints import users, locations

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

app.include_router(users.router)
app.include_router(locations.router)





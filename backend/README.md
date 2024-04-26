# Building a new image

# Running locally
`python3 -m uvicorn main:app --reload`

# Build new image
`docker build . -t backend `

# Run in Docker
`docker run --name backend --rm  --network my-project-network -p 8000:8000 backend`

# Database
Uses Alembic for database migrations
- Make changes to database models
- run `alembic revision --autogenerate -m "{some message}"`
- check the version and make sure everything looks right
- run `alembic upgrade head` to run all migrations
- to reverse all migrations, run `alembic downgrade base`
- to reverse specific migration, run `alembic downgrade {version}`
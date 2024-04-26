# import psycopg2
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# def get_engine():
#     url = f"postgresql://localhost:5432/myprojectdb"
#     return create_engine(url, pool_size=50, echo=False)

# def get_session():
#     engine = get_engine()
#     return sessionmaker(bind=engine)

# connection = psycopg2.connect(
#     host = "localhost",
#     database = "myprojectdb",
#     user = "josephkalbacher",
# )
# cursor = connection.cursor()

# connection.close()
#!----------------------------------
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# from model.Userdb import Base
from db.Userdb import Base


load_dotenv()
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_DIALECT = os.getenv("DB_DIALECT")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_USER = os.getenv("DB_USER")
DB_PORT = os.getenv("DB_PORT")


# todo lo referente a la conexion
URL_CONECTION = f"{DB_DIALECT}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(
    URL_CONECTION,
)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

# esto es para crear la base de datos
Base.metadata.create_all(bind=engine)
SessionLocal.close_all()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

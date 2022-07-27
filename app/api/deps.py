from typing import Generator
from app.db.session import engine
from sqlmodel import Session


def get_db() -> Generator:
    try:
        db = Session(engine)
        yield db
    finally:
        db.close()

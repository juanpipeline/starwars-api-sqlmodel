from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel
import datetime as dt


# Species models


class SpecieBase(SQLModel):
    name: str
    designation: str
    average_lifespan: float
    average_height: float
    language: str
    skin_color: str


class Specie(SpecieBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: dt.datetime = Field(default_factory=dt.datetime.utcnow, nullable=False)
    updated_at: Optional[dt.datetime] = Field(
        default=None, sa_column_kwargs={"onupdate": dt.datetime.utcnow}, nullable=True
    )
    characters: List["Character"] = Relationship(back_populates="specie")  # noqa # type: ignore


class SpecieRead(SpecieBase):
    id: int
    created_at: dt.datetime
    updated_at: Optional[dt.datetime] = None


class SpecieCreate(SpecieBase):
    pass


class SpecieUpdate(SQLModel):
    name: Optional[str] = None
    designation: Optional[str] = None
    average_lifespan: Optional[float] = None
    average_height: Optional[float] = None
    language: Optional[str] = None
    skin_color: Optional[str] = None


class SpecieSearchParams(SQLModel):
    name: Optional[str] = None
    designation: Optional[str] = None
    average_lifespan: Optional[float] = None
    average_height: Optional[float] = None
    language: Optional[str] = None
    skin_color: Optional[str] = None

from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
import datetime as dt
from app.models.species import Specie, SpecieRead

# Characters models


class CharacterBase(SQLModel):
    hair_color: str
    height: float
    mass: float
    name: str
    skin_color: str
    specie_id: Optional[int] = Field(default=None, foreign_key="specie.id")


class Character(CharacterBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    specie: Optional[Specie] = Relationship(back_populates="characters")
    created_at: dt.datetime = Field(default_factory=dt.datetime.utcnow, nullable=False)
    updated_at: Optional[dt.datetime] = Field(
        default=None, sa_column_kwargs={"onupdate": dt.datetime.utcnow}, nullable=True
    )


class CharacterRead(CharacterBase):
    id: int
    specie: Optional[SpecieRead] = None
    created_at: dt.datetime
    updated_at: Optional[dt.datetime] = None


class CharacterCreate(CharacterBase):
    pass


class CharacterUpdate(SQLModel):
    hair_color: Optional[str] = None
    height: Optional[float] = None
    mass: Optional[float] = None
    name: Optional[str] = None
    skin_color: Optional[str] = None
    species_id: Optional[int] = None


class CharacterSearchParams(SQLModel):
    hair_color: Optional[str] = None
    height: Optional[float] = None
    mass: Optional[float] = None
    name: Optional[str] = None
    skin_color: Optional[str] = None

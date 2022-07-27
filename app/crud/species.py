from app.crud.base import CRUDBase
from app.models.species import (
    Specie,
    SpecieCreate,
    SpecieUpdate,
    SpecieSearchParams,
)


class CRUDSpecies(
    CRUDBase[Specie, Specie, SpecieCreate, SpecieUpdate, SpecieSearchParams]
):
    pass


specie = CRUDSpecies(Specie)

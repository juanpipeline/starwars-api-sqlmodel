from app.crud.base import CRUDBase
from app.models.characters import (
    Character,
    CharacterRead,
    CharacterCreate,
    CharacterUpdate,
    CharacterSearchParams,
)


class CRUDCharacters(
    CRUDBase[
        Character,
        CharacterRead,
        CharacterCreate,
        CharacterUpdate,
        CharacterSearchParams,
    ]
):
    pass


character = CRUDCharacters(Character)

from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
import app.models.characters as schemas
from pygination import paginate
from pygination.models import PageModel
from pygination.errors import PaginationError

router = APIRouter()


@router.get("/{id}", response_model=schemas.CharacterRead)
def read_character(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get item by ID.
    """
    character = crud.character.get(db=db, id=id)
    if not character:
        raise HTTPException(status_code=404, detail="character not found")
    return character


@router.patch("/{id}", response_model=schemas.Character)
def update_character(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    character_in: schemas.CharacterUpdate,
) -> Any:
    """
    Update an item.
    """
    character = crud.character.get(db=db, id=id)
    if not character:
        raise HTTPException(status_code=404, detail="character not found")
    character = crud.character.update(db=db, db_obj=character, obj_in=character_in)
    return character


@router.delete("/{id}", response_model=schemas.Character)
def delete_character(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Delete an item.
    """
    character = crud.character.get(db=db, id=id)
    if not character:
        raise HTTPException(status_code=404, detail="character not found")
    character = crud.character.remove(db=db, id=id)
    return character


@router.post("", response_model=schemas.Character)
def create_character(
    *,
    db: Session = Depends(deps.get_db),
    body: schemas.CharacterCreate,
) -> Any:
    """
    Get item by ID.
    """
    character = crud.character.create(db=db, obj_in=body)
    if not character:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="character could not be created",
        )
    return character


@router.get("", response_model=PageModel[schemas.CharacterRead])
def read_characters(
    *,
    db: Session = Depends(deps.get_db),
    page: int = 0,
    size: int = 50,
    params: schemas.CharacterSearchParams = Depends(),
) -> Any:
    """
    Get item by ID.
    """
    characters_query = crud.character.get_multi_query(db=db, search_params=params)

    try:
        pygination_page = paginate(characters_query, page, size)
    except (PaginationError, AttributeError) as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    characters_page = PageModel[schemas.CharacterRead].from_orm(pygination_page)
    return characters_page

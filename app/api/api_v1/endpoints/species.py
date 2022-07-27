from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
import app.models.species as schemas
from pygination import paginate
from pygination.models import PageModel
from pygination.errors import PaginationError

router = APIRouter()


@router.get("/{id}", response_model=schemas.Specie)
def read_specie(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get item by ID.
    """
    specie = crud.specie.get(db=db, id=id)
    if not specie:
        raise HTTPException(status_code=404, detail="specie not found")
    return specie


@router.patch("/{id}", response_model=schemas.Specie)
def update_specie(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    specie_in: schemas.SpecieUpdate,
) -> Any:
    """
    Update an item.
    """
    specie = crud.specie.get(db=db, id=id)
    if not specie:
        raise HTTPException(status_code=404, detail="specie not found")
    specie = crud.specie.update(db=db, db_obj=specie, obj_in=specie_in)
    return specie


@router.delete("/{id}", response_model=schemas.Specie)
def delete_specie(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Delete an item.
    """
    specie = crud.specie.get(db=db, id=id)
    if not specie:
        raise HTTPException(status_code=404, detail="specie not found")
    specie = crud.specie.remove(db=db, id=id)
    return specie


@router.post("", response_model=schemas.Specie)
def create_specie(
    *,
    db: Session = Depends(deps.get_db),
    body: schemas.SpecieCreate,
) -> Any:
    """
    Get item by ID.
    """
    specie = crud.specie.create(db=db, obj_in=body)
    if not specie:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="specie could not be created",
        )
    return specie


@router.get("", response_model=PageModel[schemas.Specie])
def read_species(
    *,
    db: Session = Depends(deps.get_db),
    page: int = 0,
    size: int = 50,
    params: schemas.SpecieSearchParams = Depends(),
) -> Any:
    """
    Get item by ID.
    """
    species_query = crud.specie.get_multi_query(db=db, search_params=params)

    try:
        pygination_page = paginate(species_query, page, size)
    except (PaginationError, AttributeError) as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    species_page = PageModel[schemas.Specie].from_orm(pygination_page)
    return species_page

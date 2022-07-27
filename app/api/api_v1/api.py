from fastapi import APIRouter

from app.api.api_v1.endpoints import characters, species

api_router = APIRouter()
api_router.include_router(characters.router, prefix="/characters", tags=["Characters"])
api_router.include_router(species.router, prefix="/species", tags=["Species"])

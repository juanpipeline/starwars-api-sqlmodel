import pytest  # noqa
from fastapi.testclient import TestClient
from app.main import app
from typing import Generator, List
from sqlmodel import Session
from app.core.config import settings
from app.models.species import Specie
from app.models.characters import Character


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c


@pytest.fixture()
def specie_generated(client: TestClient, db: Session) -> Specie:
    data = {
        "name": "Yoda's specie",
        "designation": "Sentient",
        "average_lifespan": 500,
        "average_height": 100,
        "language": "Unknown",
        "skin_color": "Green",
    }

    response = client.post(
        f"{settings.API_V1_STR}/species",
        json=data,
    )

    data = response.json()

    return Specie.parse_obj(data)


@pytest.fixture()
def character_generated(
    client: TestClient, specie_generated: Specie, db: Session
) -> Specie:
    data = {
        "hair_color": "White",
        "height": 100,
        "mass": 30,
        "name": "Yoda",
        "skin_color": "Green",
        "specie_id": specie_generated.id,
    }

    response = client.post(
        f"{settings.API_V1_STR}/characters",
        json=data,
    )

    data = response.json()

    return Character.parse_obj(data)


@pytest.fixture()
def same_specie_characters_generated(
    client: TestClient, specie_generated: Specie, db: Session
) -> List[Character]:
    data = [
        {
            "hair_color": "White",
            "height": 100,
            "mass": 30,
            "name": "Yoda",
            "skin_color": "Green",
            "specie_id": specie_generated.id,
        },
        {
            "hair_color": "White",
            "height": 50,
            "mass": 10,
            "name": "Grogu",
            "skin_color": "Green",
            "specie_id": specie_generated.id,
        },
    ]

    responses = [
        client.post(
            f"{settings.API_V1_STR}/characters",
            json=character,
        )
        for character in data
    ]

    return [Character.parse_obj(data.json()) for data in responses]


@pytest.fixture()
def species_generated(client: TestClient, specie_generated: Specie) -> List[Specie]:
    data = [
        {
            "name": "Kaleesh",
            "designation": "Sentient",
            "average_lifespan": 80,
            "average_height": 180,
            "language": "Kaleesh",
            "skin_color": "red",
        },
        {
            "name": "Human",
            "designation": "Sentient",
            "average_lifespan": 100,
            "average_height": 180,
            "language": "Galactic basic standard",
            "skin_color": "Pale",
        },
    ]

    responses = [
        client.post(
            f"{settings.API_V1_STR}/species",
            json=specie,
        )
        for specie in data
    ]

    return [Specie.parse_obj(data.json()) for data in responses]

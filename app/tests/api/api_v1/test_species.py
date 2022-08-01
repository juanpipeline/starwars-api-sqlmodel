from typing import List
from fastapi.testclient import TestClient
from app.core.config import settings
from app.models.species import Specie


def test_delete_specie(
    client: TestClient,
    specie_generated: Specie,
) -> None:

    response = client.delete(f"{settings.API_V1_STR}/species/{specie_generated.id}")
    assert response.status_code == 200

    content = response.json()
    assert content["name"] == specie_generated.name
    assert content["designation"] == specie_generated.designation
    assert content["average_lifespan"] == specie_generated.average_lifespan
    assert content["language"] == specie_generated.language
    assert content["skin_color"] == specie_generated.skin_color
    assert content["average_height"] == specie_generated.average_height


def test_create_specie(
    client: TestClient,
) -> None:

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
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]
    assert content["designation"] == data["designation"]
    assert content["average_lifespan"] == data["average_lifespan"]
    assert content["average_height"] == data["average_height"]
    assert content["language"] == data["language"]
    assert content["skin_color"] == data["skin_color"]
    # Delete species
    specie_id = content["id"]
    client.delete(f"{settings.API_V1_STR}/species/{specie_id}")


def test_update_specie(
    client: TestClient,
    specie_generated: Specie,
) -> None:

    data = {
        "language": "English",
        "skin_color": "Red",
    }

    response = client.patch(
        f"{settings.API_V1_STR}/species/{specie_generated.id}",
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == specie_generated.name
    assert content["designation"] == specie_generated.designation
    assert content["average_lifespan"] == specie_generated.average_lifespan
    assert content["average_height"] == specie_generated.average_height
    assert content["language"] == data["language"]
    assert content["skin_color"] == data["skin_color"]
    # Delete species
    client.delete(f"{settings.API_V1_STR}/species/{specie_generated.id}")


def test_read_specie(
    client: TestClient,
    specie_generated: Specie,
) -> None:

    response = client.get(f"{settings.API_V1_STR}/species/{specie_generated.id}")
    assert response.status_code == 200

    content = response.json()
    assert content["name"] == specie_generated.name
    assert content["designation"] == specie_generated.designation
    assert content["average_lifespan"] == specie_generated.average_lifespan
    assert content["language"] == specie_generated.language
    assert content["skin_color"] == specie_generated.skin_color
    assert content["average_height"] == specie_generated.average_height
    # Delete species
    client.delete(f"{settings.API_V1_STR}/species/{specie_generated.id}")


class TestSearchSpecies:
    def test_search_specie_by_name(
        self,
        client: TestClient,
        species_generated: List[Specie],
    ) -> None:

        first_specie = species_generated[0]

        response = client.get(
            f"{settings.API_V1_STR}/species", params={"name": first_specie.name}
        )

        assert response.status_code == 200
        specie_page = response.json()

        assert len(specie_page["items"]) == 1
        first_specie_in_page = specie_page["items"][0]
        assert first_specie_in_page["name"] == first_specie.name
        [
            client.delete(f"{settings.API_V1_STR}/species/{specie.id}")
            for specie in species_generated
        ]

    def test_search_specie_by_language(
        self,
        client: TestClient,
        species_generated: List[Specie],
    ) -> None:

        first_specie = species_generated[0]

        response = client.get(
            f"{settings.API_V1_STR}/species", params={"language": first_specie.language}
        )

        assert response.status_code == 200
        specie_page = response.json()

        assert len(specie_page["items"]) == 1
        first_specie_in_page = specie_page["items"][0]
        assert first_specie_in_page["language"] == first_specie.language
        [
            client.delete(f"{settings.API_V1_STR}/species/{specie.id}")
            for specie in species_generated
        ]

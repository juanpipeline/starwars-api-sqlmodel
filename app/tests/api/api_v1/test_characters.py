from typing import List
from fastapi.testclient import TestClient
from app.core.config import settings
from app.models.species import Specie
from app.models.characters import Character


def test_delete_character(client: TestClient, character_generated: Character) -> None:

    response = client.delete(
        f"{settings.API_V1_STR}/characters/{character_generated.id}"
    )
    assert response.status_code == 200
    content = response.json()
    assert content["hair_color"] == character_generated.hair_color
    assert content["height"] == character_generated.height
    assert content["mass"] == character_generated.mass
    assert content["skin_color"] == character_generated.skin_color
    assert content["specie_id"] == character_generated.specie_id


def test_create_character(
    client: TestClient,
    specie_generated: Specie,
) -> None:

    data = {
        "hair_color": "white",
        "height": 100,
        "mass": 30,
        "name": "Yoda",
        "skin_color": "green",
        "specie_id": specie_generated.id,
    }

    response = client.post(
        f"{settings.API_V1_STR}/characters",
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["hair_color"] == data["hair_color"]
    assert content["height"] == data["height"]
    assert content["mass"] == data["mass"]
    assert content["skin_color"] == data["skin_color"]
    assert content["specie_id"] == data["specie_id"]

    # Delete character and specie
    content_id = content["id"]
    client.delete(f"{settings.API_V1_STR}/characters/{content_id}")
    client.delete(f"{settings.API_V1_STR}/species/{specie_generated.id}")


def test_read_character(
    client: TestClient,
    character_generated: Character,
) -> None:

    response = client.get(f"{settings.API_V1_STR}/characters/{character_generated.id}")
    assert response.status_code == 200
    content = response.json()
    assert content["hair_color"] == character_generated.hair_color
    assert content["height"] == character_generated.height
    assert content["mass"] == character_generated.mass
    assert content["skin_color"] == character_generated.skin_color
    assert content["specie_id"] == character_generated.specie_id

    # Delete character and specie
    client.delete(f"{settings.API_V1_STR}/characters/{character_generated.id}")
    client.delete(f"{settings.API_V1_STR}/species/{character_generated.specie_id}")


def test_update_character(
    client: TestClient,
    character_generated: Character,
) -> None:

    data = {
        "height": 120,
        "mass": 10,
        "skin_color": "Yellow",
    }

    response = client.patch(
        f"{settings.API_V1_STR}/characters/{character_generated.id}",
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["height"] == data["height"]
    assert content["mass"] == data["mass"]
    assert content["skin_color"] == data["skin_color"]

    # Delete character and specie
    client.delete(f"{settings.API_V1_STR}/characters/{character_generated.id}")
    client.delete(f"{settings.API_V1_STR}/species/{character_generated.specie_id}")


class TestSearchCharactes:
    def test_search_character_by_name(
        self,
        client: TestClient,
        same_specie_characters_generated: List[Character],
    ) -> None:

        first_character = same_specie_characters_generated[0]

        response = client.get(
            f"{settings.API_V1_STR}/characters", params={"name": first_character.name}
        )

        assert response.status_code == 200
        character_page = response.json()

        assert len(character_page["items"]) == 1
        first_character_in_page = character_page["items"][0]
        assert first_character_in_page["name"] == first_character.name
        [
            client.delete(f"{settings.API_V1_STR}/characters/{character.id}")
            for character in same_specie_characters_generated
        ]
        client.delete(
            f"{settings.API_V1_STR}/species/{same_specie_characters_generated[0].specie_id}"
        )

    def test_search_character_by_height(
        self,
        client: TestClient,
        same_specie_characters_generated: List[Character],
    ) -> None:

        first_character = same_specie_characters_generated[0]

        response = client.get(
            f"{settings.API_V1_STR}/characters",
            params={"height": first_character.height},
        )

        assert response.status_code == 200
        character_page = response.json()

        assert len(character_page["items"]) == 1
        first_character_in_page = character_page["items"][0]
        assert first_character_in_page["height"] == first_character.height
        [
            client.delete(f"{settings.API_V1_STR}/characters/{character.id}")
            for character in same_specie_characters_generated
        ]
        client.delete(
            f"{settings.API_V1_STR}/species/{same_specie_characters_generated[0].specie_id}"
        )

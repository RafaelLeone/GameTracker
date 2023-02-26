from http import HTTPStatus

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile

from gametracker.games.models import Game


@pytest.fixture
def game(db):
    return Game.objects.create(
        title="Tonylamkins e seus teclados",
        platform="Tonylamkins",
        cover="url",
        status=1
    )


def test_list_games_retur_games_listl(client, db):
    game = Game.objects.create(
        title="Tonylamkins e seus teclados",
        platform="Tonylamkins",
        cover="url",
        status=1
    )

    resp = client.post("/api/games/list_games")
    assert resp.json() == {"games": [game.to_dict_json()]}
    assert resp.status_code == HTTPStatus.OK


def test_add_game_create_a_game(client, db):
    resp = client.post(
        "/api/games/add_game",
        {
            "title": "We are the djavue",
            "platform": "Tonylampkins",
            "cover": "https://www.lumitecfoto.com.br/media/catalog/product/cache/1/image/578x/9df78eab33525d08d6e5fb8d27136e95/l/a/lampada-incandescente-100w-1_1.jpg",
        },
    )
    assert resp.json() == Game.objects.get(title="We are the djavue").to_dict_json()
    assert resp.status_code == HTTPStatus.OK


def test_delete_game(client, db, game):
    resp = client.post(
        "/api/games/delete_game",
        {
            "id": game.id
        },
    )
    assert Game.objects.all().count() == 0
    assert resp.status_code == HTTPStatus.OK

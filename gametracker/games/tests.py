import pdb
from http import HTTPStatus

import pytest
from gametracker.games.models import Game
from model_bakery import baker


@pytest.fixture
def game(db):
    return Game.objects.create(
        title="Tonylamkins e seus teclados",
        platform="Tonylamkins",
        cover="url",
        timer=10,
        status=1
    )


def test_list_games_return_games_listl(client, db):
    game = Game.objects.create(
        title="Tonylamkins e seus teclados",
        platform="Tonylamkins",
        cover="url",
        timer=100,
        status=1
    )

    resp = client.post("/api/games/list_games")
    assert resp.json() == {"games": [game.to_dict_json()]}
    assert resp.status_code == HTTPStatus.OK


def test_add_game_create_a_game(client, db, game):
    resp = client.post(
        "/api/games/add_game",
        {
            "title": "We are the djavue",
            "platform": "ESSE TA INTEIRO",
            "cover": "https://www.lumitecfoto.com.br/media/catalog/product/cache/1/image/578x/9df78eab33525d08d6e5fb8d27136e95/l/a/lampada-incandescente-100w-1_1.jpg",
            "timer": 100
        },
    )
    expected_json = Game.objects.get(title="We are the djavue").to_dict_json() # Fazer devolver o timer como inteiro
    expected_json['timer'] = str(expected_json['timer'])
    assert resp.json() == expected_json
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


def test_change_status(client, db, game):
    new_status = game.status + 1
    resp = client.post(
        "/api/games/change_status",
        {
            "id": game.id,
            "new_status": new_status
        },
    )
    game.refresh_from_db()
    assert game.status == new_status
    assert resp.status_code == HTTPStatus.OK


def test_calculate_total_hours(client, db, game):
    expected_json = game.to_dict_json()
    request = client.get('/api/games/timer').json()
    assert request['totalHours'] == expected_json['timer']


def test_calculate_hoursPlayed(client, db):
    baker.make('games.Game', status=1, _quantity=2)
    baker.make('games.Game', status=2, _quantity=2)
    game = Game.objects.create(
    title="Clara Nunes na bateria",
    platform="ClaraDaBatera",
    cover="url",
    timer=150,
    status=3
    )
    expected_json = game.to_dict_json()
    request = client.get('/api/games/timer').json()
    assert request["hoursPlayed"] == 150

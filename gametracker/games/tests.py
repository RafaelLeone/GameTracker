from http import HTTPStatus

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile

from gametracker.games.models import Game


@pytest.fixture
def song(db):
    return Game.objects.create(
        title="Tonylamkins e seus teclados",
        platform="Tonylamkins",
        cover="url",
        status=1
    )


def test_list_songs_retur_songs_listl(client, db):
    song = Game.objects.create(
        title="Tonylamkins e seus teclados",
        platform="Tonylamkins",
        cover="url",
        status=1
    )

    resp = client.post("/api/games/list_songs")
    assert resp.json() == {"songs": [song.to_dict_json()]}
    assert resp.status_code == HTTPStatus.OK


def test_add_song_create_a_song(client, db):
    resp = client.post(
        "/api/games/add_song",
        {
            "title": "We are the djavue",
            "platform": "Tonylampkins",
            "cover": "https://www.lumitecfoto.com.br/media/catalog/product/cache/1/image/578x/9df78eab33525d08d6e5fb8d27136e95/l/a/lampada-incandescente-100w-1_1.jpg",
        },
    )
    assert resp.json() == Game.objects.get(title="We are the djavue").to_dict_json()
    assert resp.status_code == HTTPStatus.OK


def test_delete_song(client, db, song):
    resp = client.post(
        "/api/games/delete_song",
        {
            "id": song.id
        },
    )
    assert Game.objects.all().count() == 0
    assert resp.status_code == HTTPStatus.OK

from ..models import Game


def add_song(new_song):
    song = Game(
        title=new_song["title"],
        platform=new_song["platform"],
        cover=new_song["cover"],
        status=1
    )
    song.save()
    return song.to_dict_json()


def list_songs():
    songs = Game.objects.all()

    return [song.to_dict_json() for song in songs]


def delete_song(id: int):
    Game.objects.get(id=id).delete()


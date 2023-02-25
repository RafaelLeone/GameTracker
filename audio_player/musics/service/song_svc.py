from ..models import Song


def add_song(new_song):
    song = Song(
        title=new_song["title"],
        artist=new_song["artist"],
        cover=new_song["cover"],
        status=1
    )
    song.save()
    return song.to_dict_json()


def list_songs():
    songs = Song.objects.all()

    return [song.to_dict_json() for song in songs]


def delete_song(id: int):
    Song.objects.get(id=id).delete()


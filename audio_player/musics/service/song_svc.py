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

def edit_song(editted_song):
    if editted_song["status"] == 3:
        status_now = 1
    else:
        status_now = editted_song["status"] + 1
    song = Song(
        title=editted_song["title"],
        artist=editted_song["artist"],
        cover=editted_song["cover"],
        status=status_now
    )
    song.save()
    return song.to_dict_json()


def list_songs():
    songs = Song.objects.all()

    return [song.to_dict_json() for song in songs]

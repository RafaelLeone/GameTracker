from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    cover = models.URLField(max_length=200)
    class Status(models.IntegerChoices):
        Backlog = 1
        Playing = 2
        Done = 3
    status = models.IntegerField(choices=Status.choices)

    def to_dict_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "artist": self.artist,
            "cover": self.cover,
            "status": 1
        }


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    songs = models.ManyToManyField(Song)
    created_at = models.DateTimeField("criado em", auto_now_add=True)

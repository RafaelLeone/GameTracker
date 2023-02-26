from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    cover = models.URLField(max_length=2000)
    class Status(models.IntegerChoices):
        Backlog = 1
        Playing = 2
        Done = 3
    status = models.IntegerField(choices=Status.choices)

    def to_dict_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "platform": self.platform,
            "cover": self.cover,
            "status": 1
        }

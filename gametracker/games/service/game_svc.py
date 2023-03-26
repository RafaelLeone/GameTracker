from django.db.models import Sum

from ..models import Game


def add_game(new_game):
    game = Game(
        title=new_game["title"],
        platform=new_game["platform"],
        cover=new_game["cover"],
        timer=new_game["timer"],
        status=1
    )
    game.save()
    return game.to_dict_json()


def list_games():
    games = Game.objects.all().order_by("id")

    return [game.to_dict_json() for game in games]


def delete_game(id: int):
    Game.objects.get(id=id).delete()


def change_status(id: int, status: int):
    Game.objects.filter(id=id).update(status=status)

def get_total_hours():
    totalHours = Game.objects.aggregate(Sum('timer'))['timer__sum']
    hoursPlayed = Game.objects.filter(status=3).aggregate(total=Sum('timer'))['total']
    hoursPlayed = 0 if hoursPlayed is None else hoursPlayed
    timer = {"totalHours": totalHours, "hoursPlayed": hoursPlayed}
    return timer



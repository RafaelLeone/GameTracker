from ..models import Game


def add_game(new_game):
    game = Game(
        title=new_game["title"],
        platform=new_game["platform"],
        cover=new_game["cover"],
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



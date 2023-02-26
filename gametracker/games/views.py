from django.http import JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt

from .service import game_svc


@csrf_exempt
def add_game(request):
    game_qrdct = QueryDict("", mutable=True)
    game_qrdct.update(request.POST)
    game_qrdct.update(request.FILES)
    game = game_svc.add_game(game_qrdct)

    return JsonResponse(game)


def list_games(request):
    games = game_svc.list_games()
    return JsonResponse({"games": games})


@csrf_exempt
def delete_game(request):
    id = request.POST["id"]
    game_svc.delete_game(id)
    return JsonResponse({})

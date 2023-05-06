from django.shortcuts import render
from django.http import HttpResponse
from .models import Players

TEMPLATE_DIRS = 'os.path.join(BASE_DIR, "templates").'


def index(request):
    context = {}
    players = Players.objects.order_by("-overall_elo")[:10]
    context["players"] = players
    context["showFullList"] = False

    return render(request, "index.html", context)


def list(request):
    context = {}
    players = Players.objects.all().order_by("-overall_elo")
    context["players"] = players
    context["showFullList"] = True

    return render(request, "index.html", context)

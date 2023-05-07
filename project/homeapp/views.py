from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Players
from .models import Locations
import json

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
    locations = serializers.serialize("json", Locations.objects.all(), fields=["lat", "lng"])
    context["players"] = players
    context["locations"] = locations
    context["showFullList"] = True

    return render(request, "index.html", context)
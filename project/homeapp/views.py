from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Players
from .models import Locations
import json

TEMPLATE_DIRS = 'os.path.join(BASE_DIR, "templates").'


def index(request):
    context = {}
    players = Players.objects.all().order_by("-overall_elo")
    # locations = list(Locations.objects.values('lat', 'lng'))
    locations = serializers.serialize("json", Locations.objects.all(), fields=["lat", "lng"])

    context["players"] = players
    context["locations"] = locations

    return render(request, "index.html", context)

# def getLocations(request):
#     Locations = Locations.objects.all()
#     context = {
#         'locations': Locations,
#     }
#     return JsonResponse(context)

# def getLocations(request):
#     context = {'locations': Locations}
#     return render(request, 'index.html', context=context)
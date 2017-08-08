from django.shortcuts import render
from django.http import HttpResponse
from Light.sensor import lightSensor
# Create your views here.


def index(request):
    return render(request, "index.html")
    # return HttpResponse("Hello light view " + str(lightSensor()))


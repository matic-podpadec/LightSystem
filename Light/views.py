from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.template import loader
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.shortcuts import redirect
from django.core import serializers
from .forms import LightControlForm, LightAddForm, GroupAddForm
from .lights import single_light_control, light_add_to_db, light_get_all
from .groups import group_add_to_db, group_get_all
from .models import Light, LightGroup
import re
import _thread

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Registered: " + form.cleaned_data['username'])

    else:
        form = UserCreationForm()

    return render(request, 'index.html', {'form': form})

    # return render(request, "index.html")
    # return HttpResponse("Hello light view " + str(lightSensor()))


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Registered: " + form.cleaned_data['username'])

    else:
        form = UserCreationForm()

    return render(request, 'index.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request=None, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect(menu)

        else:
            return HttpResponse("Fuck of m8")

    form = AuthenticationForm()
    return render(request, 'index.html', {'form': form})


@login_required
def menu(request):
    return render(request, 'menu.html')


@login_required
def light_control(request):
    lights = Light.objects.all()
    st = ""
    for light in lights:
        st += light.name

    return HttpResponse(st)
    """    
    form = LightControlForm()

    if request.method == 'POST':
        _thread.start_new(single_light_control, (14, request.POST['intensity']))
        return render(request, "light_control.html", {'form': form})

    return render(request, 'light_control.html', {'form': form})

class LightsList(ListView):
    model = Light
"""


@login_required
def light_add(request):
    form = LightAddForm()

    if request.method == 'POST':
        name = request.POST['name']
        pin = int(request.POST['pin'])
        light_add_to_db(name, pin)
        return HttpResponse("Light Saved")

    return render(request, 'light_add.html', {'form': form})


def light_single(request):
    pin = re.search(r'\d+', request.path).group()
    light = Light.objects.get(pin=str(pin))
    return HttpResponse(light)


def light_index(request):
    lights = Light.objects.all()
    template = loader.get_template("light_index.html")
    context = {
        'lights': lights,
    }
    return HttpResponse(template.render(context, request))


def light_form(request):
    if request.method == 'POST':
        light_pin = int(request.POST['pin'])
        light = Light.objects.filter(pin=light_pin)

        form = LightControlForm(initial={
            'id': light.id,
            'name': light.name,
            'status': light.status,
            'pin': light.pin
        })

        return render('light_control', {'form': form})

    else:
        return HttpResponse("no worky")


def light_managment(request):
    lights = light_get_all()
    json = serializers.serialize("json", lights)
    return HttpResponse(json)


def group_add(request):
    form = GroupAddForm()

    if request.method == 'POST':
        name = str(request.POST['name'])
        group_add_to_db(name)
        return HttpResponse("Group saved")

    return render(request, 'group_add.html', {'form': form})


def group_managment(request):
    groups = group_get_all()
    print(groups[0].name)

    names = groups.values_list("name")
    print(names)

    json = serializers.serialize("json", groups)
    print(json)
    return HttpResponse(json)


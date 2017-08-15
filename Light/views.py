from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.shortcuts import redirect
from .forms import LightControlForm, AddLightForm
from .lights import single_light_control
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
    form = LightControlForm()

    if request.method == 'POST':
        _thread.start_new(single_light_control, (14, request.POST['intensity']))
        return render(request, "light_control.html", {'form': form})

    return render(request, 'light_control.html', {'form': form})


@login_required
def light_add(request):
    form = LightAddForm()

    if request.method == 'POST':
        light_add(request.POST['name'], request.POST['pin'])
        return HttpResponse("Light Saved")

    return render(request, 'light_add.html', {'form': form})

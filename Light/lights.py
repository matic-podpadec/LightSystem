import time
from .models import Light


def single_light_control(a, b):
    time.sleep(5)


def light_add_to_db(name, pin):
    light = Light.create(name, pin)
    light.save()


def light_get_all():
    lights = Light.objects.all()
    return lights

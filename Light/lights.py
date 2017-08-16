
import RPi.GPIO as GPIO
import sys
import time
from .models import Light


def single_light_control(a, b):
    GPIO.setmode(GPIO.BCM)

    pin = int(a)
    intensity = float(b)

    GPIO.setup(pin, GPIO.OUT)
    light = GPIO.PWM(pin, 100)

    light.start(intensity)
    time.sleep(5)


def light_add_to_db(name, pin):
    light = Light.create(name, pin)
    light.save()


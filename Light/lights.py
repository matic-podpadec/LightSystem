import RPi.GPIO as GPIO
import sys
import time


def single_light_control(a, b):
    GPIO.setmode(GPIO.BCM)

    pin = int(a)
    intensity = float(b)

    GPIO.setup(pin, GPIO.OUT)
    light = GPIO.PWM(pin, 100)

    light.start(intensity)
    time.sleep(5)
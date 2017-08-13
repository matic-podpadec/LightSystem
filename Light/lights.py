import RPi.GPIO as GPIO
import sys
import time


class SingleLightControl(pin, intensity):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

    light = GPIO.PWM(pin, intensity)
    light.start(0)

import RPi.GPIO as GPIO
import sys
import time


def single_light_control(a, b):
    # GPIO.setmode(GPIO.BCM)
    pin = int(a)
    intensity = float(b)

    if GPIO.gpio_function(pin) is not GPIO.OUT:
        GPIO.setup(pin, GPIO.OUT)
        light = GPIO.PWM(pin, 100)
        light.start(intensity)

    else:
        if intensity > 0:
            light.ChangeDutyCycle(intensity)

        else:
            GPIO.cleanup()

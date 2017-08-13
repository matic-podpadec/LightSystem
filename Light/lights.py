import RPi.GPIO as GPIO
import sys
import time


def single_light_control(pin, intensity):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

    light = GPIO.PWM(pin, 100)
    light.start(intensity)

    time.sleep(3)

    GPIO.cleanup()

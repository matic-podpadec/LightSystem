import RPi.GPIO as GPIO
import sys
import time


def single_light_control(pin, intensity):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

    light = GPIO.PWM(pin, 100)
    light.start(0)

    dc = 0

    while dc <= 100:
        light.ChangeDutyCycle(dc)
        time.sleep(1)
        dc += 20

    GPIO.cleanup()

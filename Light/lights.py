import RPi.GPIO as GPIO


def single_light_control(pin, intensity):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

    light = GPIO.PWM(pin, intensity)
    light.start(0)

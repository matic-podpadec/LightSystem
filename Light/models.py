from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import time

# Create your models here.


class Setting(models.Model):
    name = models.CharField(max_length=32)

    @classmethod
    def __str__(self):
        return self.name


class LightGroup(models.Model):
    name = models.CharField(max_length=32)
    setting = models.ForeignKey(
        Setting,
        models.SET_NULL,
        null=True,
        default=0,
    )

    @classmethod
    def create(cls, name):
        group = cls(name=name, setting=0)
        return group

    def __str__(self):
        return self.name


class Light(models.Model):
    # Name of our light
    name = models.CharField(max_length=32)

    # Power represents intensity of light
    status = models.SmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    pin = models.SmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(13)],
        unique=True
    )
    group = models.ForeignKey(
        LightGroup,
        models.SET_NULL,
        blank=True,
        null=True,
    )

    @classmethod
    def create(cls, name, pin):
        light = cls(name=name, pin=pin, status=0)
        return light

    def __str__(self):
        return self.name + ": " + str(self.status)


class Sensor(models.Model):
    name = models.CharField(max_length=32)
    pin = models.SmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )

    group = models.ForeignKey(
        LightGroup,
        models.SET_NULL,
        blank=True,
        null=True,
    )

    @classmethod
    def __str__(self):
        return self.name


class Schedule(models.Model):
    name = models.CharField(max_length=32)
    inUse = models.BooleanField(default=0)
    time = models.DateTimeField(default=time.time())
    group = models.ForeignKey(
        LightGroup,
        models.SET_NULL,
        blank=True,
        null=True,
    )
    setting = models.IntegerField(default=0)

    @classmethod
    def __str__(self):
        return self.name

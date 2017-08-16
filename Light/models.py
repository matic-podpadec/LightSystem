from django.db import models
from django.contrib.auth.models import User, Group
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Light(models.Model):
    name = models.CharField(max_length=32)
    status = models.SmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    pin = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(26)]
    )
    group = models.ForeignKey(Group)

    @classmethod
    def create(cls, name, pin):
        light = cls(name=name, pin=pin)
        return light

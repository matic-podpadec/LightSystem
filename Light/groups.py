import time
from .models import LightGroup


def single_light_control(a, b):
    time.sleep(5)


def group_add_to_db(name):
    group = LightGroup.create(name)
    group.save()


def group_get_all():
    groups = LightGroup.objects.all()
    return groups

"""
class Group(models.Model):
    name = models.CharField(max_length=32)
    setting = models.SmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(2)]
    )

"""
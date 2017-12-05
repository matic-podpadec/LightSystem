from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Light)
admin.site.register(Sensor)
admin.site.register(Schedule)
admin.site.register(LightGroup)
admin.site.register(Setting)

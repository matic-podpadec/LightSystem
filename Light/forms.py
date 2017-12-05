from django import forms
from django.forms import ModelForm
from Light.models import Light, LightGroup


class LightControlForm(forms.Form,):
    intensity = forms.IntegerField(100, 0)


class LightAddForm(ModelForm):
    class Meta:
        model = Light
        fields = ['name', 'pin']


class GroupAddForm(ModelForm):
    class Meta:
        model = LightGroup
        fields = ["name"]

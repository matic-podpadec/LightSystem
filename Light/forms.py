from django import forms
from django.forms import ModelForm
from Light.models import Light


class LightControlForm(forms.Form):
    intensity = forms.IntegerField(100, 0)


class AddLightForm(ModelForm):
    class Meta:
        model = Light
        fields = ['name', 'pin']

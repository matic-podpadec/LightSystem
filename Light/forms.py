from django import forms


class LightControlForm(forms.Form):
    intensity = forms.IntegerField(100, 0)

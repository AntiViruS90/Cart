from django import forms
from django.core.validators import RegexValidator


class Myforms(forms.Form):
    address = forms.CharField()
    name = forms.CharField()
    telephone = forms.CharField(
        validators=[RegexValidator('[+7][0-9]{10}', message='Please enter valid number')]
    )
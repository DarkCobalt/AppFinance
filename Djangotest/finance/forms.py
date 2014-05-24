__author__ = 'cobalt'
from django import forms

class Date(forms.Form):
    start = forms.DateField()
    end = forms.DateField()
__author__ = 'cobalt'
from django import forms

class Date(forms.Form):
    start = forms.CharField(max_length=100)
    end = forms.CharField()
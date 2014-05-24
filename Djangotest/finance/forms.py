__author__ = 'cobalt'
from django import forms


class Date(forms.Form):
    TICKER_CHOICES = {
        ('YHOO', 'Yahoo'),
        ('GOOGL', 'Google'),
    }
    tickers = forms.ChoiceField(choices=TICKER_CHOICES)
    start = forms.DateField()
    end = forms.DateField()
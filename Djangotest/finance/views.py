from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from pprint import pprint
from yahoo_finance import Share
from django.shortcuts import render
from forms import Date

# Create your views here.

LIST = {
    ('YHOO', 'Yahoo'),
    ('GOOGL', 'Google'),
}

def index(request):
    yahoo = Share('YHOO')
    if request.method == 'POST':
        form = Date(request.POST)
        if form.is_valid():
            g = yahoo.get_historical(form.start, form.end)
            return HttpResponseRedirect('/thanks/', g)
    else:
        form = Date()

    return render(request, 'finance/index.html', {'form': form})

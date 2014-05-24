from django.http import HttpResponse
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
            date_start = form.cleaned_data['start']
            date_end = form.cleaned_data['end']
            g = yahoo.get_historical(date_start, date_end)
            return HttpResponse(g)
    else:
        form = Date()

    return render(request, 'finance/index.html', {'form': form})

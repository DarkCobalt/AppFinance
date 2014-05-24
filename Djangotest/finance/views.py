from django.http import HttpResponse
from yahoo_finance import Share
from django.shortcuts import render
from forms import Date

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = Date(request.POST)
        if form.is_valid():
            date_start = form.cleaned_data['start']
            date_end = form.cleaned_data['end']
            ticker = form.cleaned_data['tickers']
            share = Share(ticker)
            respond = share.get_historical(date_start, date_end)
            return HttpResponse(respond)
    else:
        form = Date()

    return render(request, 'finance/index.html', {'form': form})

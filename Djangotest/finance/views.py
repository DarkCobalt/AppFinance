from django.shortcuts import render
from forms import Date

import time
from yahoo_finance import Share


def to_chartit_json(json):
    chartit_json = []
    for d in json:
            chartit_json.append([
                str(int(time.mktime(time.strptime(d['Date'], "%Y-%m-%d")))),
                float(d['Open']),
                float(d['High']),
                float(d['Low']),
                float(d['Close']),
            ])
    chartit_json.reverse()
    return chartit_json


def index(request):
    if request.method == 'POST':
        form = Date(request.POST)
        if form.is_valid():
            date_start = form.cleaned_data['start']
            date_end = form.cleaned_data['end']
            ticker = form.cleaned_data['tickers']
            share = Share(ticker)
            chart_data = share.get_historical(date_start, date_end)
            chart_data = to_chartit_json(chart_data)
            return render(request, 'finance/index.html', {'form': form, 'chart': chart_data})
    else:
        form = Date()

    return render(request, 'finance/index.html', {'form': form})

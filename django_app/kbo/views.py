import datetime
from django.shortcuts import render


def index(request):
    today = datetime.datetime.now().strftime("%Y%m%d")
    # today = 20170410
    return render(request, 'kbo/index.html', {'today': today})

from django.shortcuts import render
from .scraping import *
from .models import PaymentHistory

# Create your views here.


def home(request):
    Payment_History=PaymentHistory.objects.all()
    pool = data_pool()
    BTC = pool[0][0]
    BTCWORKERS = pool[0][1]
    BTCPOWER = pool[0][2]
    BTCRED = pool[0][3]
    
    LTC=pool[1][0]
    LTCWORKERS=pool[1][1]
    LTCPOWER=pool[1][2]
    LTCRED=pool[1][3]
    return render(request, 'index.html', {
        'BTC': BTC,
        'BTCWORKERS': BTCWORKERS,
        'BTCPOWER': BTCPOWER,
        'BTCRED':BTCRED,
        'LTC': LTC,
        'LTCWORKERS': LTCWORKERS,
        'LTCPOWER': LTCPOWER,
        'LTCRED':LTCRED,
        'PaymentHistory':Payment_History
    })


def about(request):
    return render(request, 'update.html')

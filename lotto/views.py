from django.shortcuts import render
from lotto.models import Lotto
import locale

# Create your views here.
def lotto_list(request):
    latest_list = Lotto.objects.all().order_by('-nth')[:30]
    locale.setlocale(locale.LC_ALL, '')

    # latest_list[0] = latest_list[1]
    # for i in range(len(latest_list)):
        # latest_list[i]['winmoney'] = latest_list[i]['winmoney']
        # latest_list[i]['winmoney'] = locale.format('%d', latest_list[i]['winmoney'], grouping=True)

    context = {'latest_list': latest_list}
    return render(request, 'lotto/lotto_list.html', context)

from django.shortcuts import render
from lotto.models import Lotto

# Create your views here.
def lotto_list(request):
    latest_list = Lotto.objects.all().order_by('-nth')[:10]

    context = {'latest_list': latest_list}
    return render(request, 'lotto/lotto_list.html', context)

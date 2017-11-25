from django.shortcuts import render
from eng.models import Sentences

# Create your views here.
def eng_today(request):
    # sentence_list = Sentences.objects.filter(pk__in=[1,4,7])

    # sentence_list[2]= Sentences.objects.filter(pk=2)
    sentence_list = Sentences.objects.all().order_by('?')[:10]
    context = {'sentence_list': sentence_list}
    return render(request, 'eng/eng_today.html', context)

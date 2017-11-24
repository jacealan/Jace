from django.shortcuts import render
from eng.models import Sentences

# Create your views here.
def eng_today(request):
    return render(request, 'eng/eng_today.html', {})

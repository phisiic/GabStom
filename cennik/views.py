from django.http import HttpResponse
from django.shortcuts import render
from .models import Zabieg

# glowna strona cennika
def index(request):
    zabiegi = Zabieg.objects.all()
    return render(request, 'index.html', {'Zabiegi': zabiegi})


def zabiegi(request):
    return HttpResponse("Nasze zabiegi:")
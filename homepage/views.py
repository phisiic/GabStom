from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='accounts:login')
def index(request):
    return render(request, 'farm/organic-farm-website-template/index.html')

def error_403_view(request):
    return render(request, 'error403/403-forbidden/src/index.html')
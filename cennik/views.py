from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from homepage.contactmail import ContactMail

from accounts.models import DoKontaktu
from .models import Zabieg

# glowna strona cennika
def index(request):
    if request.method == 'POST':
        input_email = request.POST['email_address']
        ContactMail(input_email)
        kontakt = DoKontaktu(email=input_email)
        kontakt.save()
        return render(request, 'cennik.html', {'email_address': input_email})
    return render(request, 'cennik.html')


def zabiegi(request):
    return HttpResponse("Nasze zabiegi:")
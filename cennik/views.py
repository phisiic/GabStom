from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

from accounts.models import DoKontaktu
from .models import Zabieg

# glowna strona cennika
def index(request):
    if request.method == 'POST':
        input_email = request.POST['email_address']
        send_mail(
            "Dziękujemy za kontakt!",
            "Dziękujemy użytkowniku za skorzystanie z naszej strony internetowej.\n" +
            "Już niedługo będziemy się kontaktować.\n" +
            "Do usłyszenia!\n" +
            "Gabinet Stomatologiczny MaxiDent\n",
            'gabinetmeddent@gmail.com',
            [input_email],
            fail_silently=False
        )
        kontakt = DoKontaktu(email=input_email)
        kontakt.save()
        return render(request, 'cennik.html', {'email_address': input_email})
    return render(request, 'cennik.html')


def zabiegi(request):
    return HttpResponse("Nasze zabiegi:")
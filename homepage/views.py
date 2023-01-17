from django.core.mail import send_mail
from django.shortcuts import render
from accounts.models import DoKontaktu



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
        return render(request, 'index.html', {'email_address': input_email})
    return render(request, 'index.html')

def error_403_view(request):
    return render(request, 'error403/403-forbidden/src/index.html')
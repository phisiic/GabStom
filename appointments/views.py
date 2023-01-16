from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Wizyta
from accounts.models import User
from django.contrib import messages
from django.core.mail import send_mail
from accounts.decorators import staff_only


@login_required(login_url='accounts:login')
def index(request):
    doctors = User.objects.staff()
    return render(request, 'index-appt.html', {'Doctors': doctors})


@login_required(login_url='accounts:login')
def book_view(request):
    doctors = User.objects.staff()
    if request.method == 'POST':
        day = request.POST['day']
        doctor = request.POST['doctor']
        service = request.POST['service']
        time = request.POST['time']

        if Wizyta.objects.all().filter(day=datetime.strptime(day, "%Y-%m-%d"), time=time, doctor=doctor):
            messages.info(request, 'Niepoprawna data - lekarz zajety')
            return redirect('appointments:book')

        if datetime.strptime(day, "%Y-%m-%d") <= datetime.now():
            messages.info(request, 'Niepoprawna data')
            return redirect('appointments:book')
        else:
            appt = Wizyta(user=request.user, service=service, day=day, time=time, doctor=doctor)
            appt.save()
            send_mail(
                "Wizyta dnia " + day,
                "Dziękujemy " + request.user.first_name + " za rejestracje wizyty!\n" +
                service + " w dniu " + day + " o " + time + "\n" +
                "dr " + doctor + "\n"
                "Do zobaczenia!\n"
                "Gabinet Stomatologiczny MaxiDent\n",
                'gabinetmeddent@gmail.com',
                [request.user.email],
                fail_silently=False)
            messages.info(request, "Udano się zarezerwować wizytę")
            return render(request, 'successful-appt.html', {'day': day, 'time': time, 'service': service, 'doctor': doctor, 'Doctors': doctors})
    else:
        return render(request, 'bookappt-1.html')

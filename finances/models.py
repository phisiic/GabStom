from django.db import models
from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator
from accounts.models import User
from django.utils.timezone import now

# Create your models here.


class Wydatek(models.Model):
    opis = models.CharField(max_length=80)
    koszt = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1000000.0)])
    dzien_zamowienia = models.DateField(default=now(), blank=True, verbose_name="Dzień")

    class Meta:
        verbose_name_plural = "Wydatki"


class Wplyw(models.Model):
    opis = models.CharField(max_length=80, null=True)
    uzytkownik = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    koszt = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1000000.0)])
    dzien_zamowienia = models.DateField(default=now(), blank=True, verbose_name="Dzień")

    class Meta:
        verbose_name_plural = "Wpływy"
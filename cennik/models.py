from django.db import models


class Zabieg(models.Model):
    nazwa = models.CharField(max_length=255)
    cena = models.FloatField()
    zdjecie = models.CharField(max_length=2083)

    class Meta:
        verbose_name_plural = "Zabiegi"
from django.contrib import admin
from .models import Wydatek, Wplyw
from totalsum.admin import TotalsumAdmin
from import_export.admin import ExportActionMixin

# Register your models here.

class WydatekAdmin(ExportActionMixin, TotalsumAdmin):
    list_display = ('opis', 'koszt', 'dzien_zamowienia')
    list_filter = ('dzien_zamowienia',)
    date_hierarchy = 'dzien_zamowienia'
    search_fields = ['opis', 'dzien_zamowienia']
    totalsum_list = ('koszt',)
    unit_of_measure = "zł"


class WplywAdmin(ExportActionMixin, TotalsumAdmin):
    list_display = ('opis', 'uzytkownik', 'koszt', 'dzien_zamowienia')
    list_filter = ('uzytkownik','dzien_zamowienia',)
    date_hierarchy = 'dzien_zamowienia'
    search_fields = ['opis', 'uzytkownik__first_name','uzytkownik__last_name', 'dzien_zamowienia']
    totalsum_list = ('koszt',)
    unit_of_measure = "zł"


admin.site.register(Wydatek, WydatekAdmin)
admin.site.register(Wplyw, WplywAdmin)
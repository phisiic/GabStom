from django.contrib import admin
from accounts.models import User
from .models import DoKontaktu
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm, ContactForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active',)
    list_filter = ('email', 'last_name', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser',)}
        ),
    )
    search_fields = ('email', 'last_name')
    ordering = ('email', 'last_name')


class KontaktAdmin(admin.ModelAdmin):
    add_form = ContactForm
    list_display = ('email', 'skontaktowano', 'time_ordered')


admin.site.register(User, CustomUserAdmin)
admin.site.register(DoKontaktu, KontaktAdmin)

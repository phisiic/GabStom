from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import login_view, register_view, logout_view

#   Sprawdzenie poprawności wywołanych funkcji w aplikacji 'accounts'
#   obsługujących prośby oraz odpowiedzi http
class TestUrls(SimpleTestCase):
    # sprawdzenie, która funkcja (view) zostanie wywołana
    # przy url = '.../accounts/register'
    def test_register_url_is_resolved(self):
        url = reverse('accounts:register')
        print(resolve(url).func)
        self.assertEquals(resolve(url).func, register_view)

    # sprawdzenie, która funkcja (view) zostanie wywołana
    # przy url = '.../accounts/login'
    def test_login_url_is_resolved(self):
        url = reverse('accounts:login')
        print(resolve(url).func)
        self.assertEquals(resolve(url).func, login_view)

    # sprawdzenie, która funkcja (view) zostanie wywołana
    # przy url = '.../accounts/logout'
    def test_logout_url_is_resolved(self):
        url = reverse('accounts:logout')
        print(resolve(url).func)
        self.assertEquals(resolve(url).func, logout_view)



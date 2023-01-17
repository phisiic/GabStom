from django.http import HttpResponse
from django.shortcuts import render


def staff_only():
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.is_staff:
                return view_func(request, *args, **kwargs)
            else:
                return render(request, 'error403/403-forbidden/src/i.html')
        return wrapper_func
    return decorator

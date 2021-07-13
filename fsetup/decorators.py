from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.conf import settings


def first_user_only(func):
    def wrapper(*args, **kwargs):

        try:
            count = User.objects.all().count()
        except BaseException:
            count = 0

        if count != 0:
            if settings.DEBUG:
                return render(args[1], 'setup/error.html')
            else:
                return HttpResponseNotFound()
        else:
            return func(*args, **kwargs)

    return wrapper

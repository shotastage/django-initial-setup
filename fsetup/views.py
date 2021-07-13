from django.views.generic import View
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from fsetup.db import DBSetup
from fsetup.decorators import first_user_only


def redirectview(request):
    return redirect('/initial_user_setup/welcome')


class WelcomeView(View):

    @first_user_only
    def get(self, request):
        return render(request, 'setup/welcome.html')

    @first_user_only
    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]

        User = get_user_model()
        User.objects.create_superuser(username, email, password)

        return redirect('/login/')


class DatabaseView(View):

    db = DBSetup()

    @first_user_only
    def get(self, request):

        migration_list: str = []

        for line in self.db.migration_list():
            if line != '\'':
                migration_list.append(line)

        context = {
            'cmd_result': migration_list
        }
        return render(request, 'setup/db.html', context)

    @first_user_only
    def post(self, request):

        self.db.migrate()

        return redirect('/initial_user_setup/superuser')


class InitialSetupView(View):

    @first_user_only
    def get(self, request):
        return render(request, 'setup/initial.html')

    @first_user_only
    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]

        User = get_user_model()
        User.objects.create_superuser(username, email, password)

        return redirect('/')

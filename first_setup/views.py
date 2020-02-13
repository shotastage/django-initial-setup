from django.views.generic import View
from django.shortcuts import render, redirect


from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from first_setup.db import DBSetup


class WelcomeView(View):

    def get(self, request):
        return render(request, 'setup/welcome.html')


    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]

        User = get_user_model()
        User.objects.create_superuser(username, email, password)
      
        return redirect('/login/')

class InitialSetupView(View):

    def get(self, request):
        return render(request, 'setup/initial.html')


    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]

        User = get_user_model()
        User.objects.create_superuser(username, email, password)
      
        return redirect('/login/')


class DatabaseView(View):
    def get(self, request):

        db = DBSetup()

        context = {
            'cmd_result': db.migration_list()
        }
        return render(request, 'setup/db.html', context)
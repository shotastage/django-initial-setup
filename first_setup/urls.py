from django.urls import path
from first_setup.views import (
    WelcomeView,
    InitialSetupView
)


urlpatterns = [
    path('initial_user_setup/welcome', WelcomeView.as_view(), name='welcome'),
    path('initial_user_setup/migration', InitialSetupView.as_view(), name='starts'),
    path('initial_user_setup/superuser', InitialSetupView.as_view(), name='starts'),
    path('initial_user_setup/confirm', InitialSetupView.as_view(), name='starts'),
]

from django.urls import path
from first_setup.views import (
    WelcomeView,
    InitialSetupView,
    DatabaseView,
    redirectview
)


urlpatterns = [
    path('initial_user_setup', redirectview, name='root'),
    path('initial_user_setup/welcome', WelcomeView.as_view(), name='welcome'),
    path('initial_user_setup/migration', DatabaseView.as_view(), name='migration'),
    path('initial_user_setup/superuser', InitialSetupView.as_view(), name='superuser'),
    path('initial_user_setup/confirm', InitialSetupView.as_view(), name='confirm'),
]

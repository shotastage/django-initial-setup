from django.urls import path
from setup.views import InitialSetupView

urlpatterns = [
    path('initial_user_setup/welcome', InitialSetupView.as_view(), name='starts'),
    path('initial_user_setup/migration', InitialSetupView.as_view(), name='starts'),
    path('initial_user_setup/superuser', InitialSetupView.as_view(), name='starts'),
    path('initial_user_setup/confirm', InitialSetupView.as_view(), name='starts'),
]

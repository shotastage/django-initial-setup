from django.urls import path
from setup.views import InitialSetupView

urlpatterns = [
    path('initial_user_setup/', InitialSetupView.as_view(), name='starts'),
]

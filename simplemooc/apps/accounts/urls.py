from django.urls import path
from simplemooc.apps.accounts.views import register
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('entrar/', LoginView.as_view(template_name='accounts/login.html') , name='login' ),
    path('cadastre-se/',register, name="register"),
]
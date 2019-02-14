from django.urls import path
from simplemooc.apps.accounts.views import register, dashboard, edit
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('entrar/', LoginView.as_view(template_name='accounts/login.html') , name='login' ),
    path('sair/', LogoutView.as_view(next_page='/') , name='logout' ),
    path('cadastre-se/',register, name="register"),
    path('editar/',edit, name="edit"),
    path('',dashboard, name="dashboard"),
]
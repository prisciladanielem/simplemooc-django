from django.urls import path
from simplemooc.apps.accounts.views import register, dashboard, edit,addCourse,password_reset, password_reset_confirm, edit_password
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',dashboard, name="dashboard"),
    path('entrar/', LoginView.as_view(template_name='accounts/login.html') , name='login' ),
    path('sair/', LogoutView.as_view(next_page='/') , name='logout' ),
    path('cadastre-se/',register, name="register"),
    path('editar/',edit, name="edit"),
    path('editar-senha/',edit_password, name="edit_password"),
    path('nova-senha/',password_reset, name="password_reset"),
    path('confirmar-nova-senha/<key>/',password_reset_confirm, name="password_reset_confirm"),
    path('adicionarcurso/',addCourse, name="addCourse"),
]
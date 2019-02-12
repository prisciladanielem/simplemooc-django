from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.conf import settings

#Mostra a página somente se o usuário estiver logado
@login_required
def dashboard(request):
    template_name = 'accounts/dashboard.html'

    return render(request, template_name)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save() #salva os dados no banco de dados
            user = authenticate(username = user.username, password = form.cleaned_data['password1'])
            login(request,user) #loga o usuário após se cadastrar no sistema
            return redirect('/') # redireciona para essa página após o login
    else:
        form =  RegisterForm()
    context = {
    'form':form
    }
    template_name = 'accounts/register.html'
    return render(request, template_name, context)
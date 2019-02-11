from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.conf import settings

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save() #salva os dados no banco de dados
            return redirect(settings.LOGIN_URL) # redireciona para essa página após o login
    else:
        form =  RegisterForm()
    context = {
    'form':form
    }
    template_name = 'accounts/register.html'
    return render(request, template_name, context)
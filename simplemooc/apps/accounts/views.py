from django.shortcuts import render,redirect
from .forms import RegisterForm, EditAccountForm
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

@login_required
def edit(request):
    template_name = 'accounts/edit.html'
    context = {}
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditAccountForm(instance=request.user) #Está alterando o usuário atual da sessão
            context['sucess'] = True
    else:
        form = EditAccountForm(instance=request.user) # se não for post, formulaŕio vazio
    context['form'] = form
    return render(request, template_name, context)
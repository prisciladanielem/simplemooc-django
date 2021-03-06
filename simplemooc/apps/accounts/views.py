from django.shortcuts import render,redirect, get_object_or_404

from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm

from django.contrib import messages

from simplemooc.apps.courses.models import Enrollment

from .forms import RegisterForm, PasswordResetForm, EditAccountForm, AddCoursesForm
from .models import PasswordReset

User = get_user_model()

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
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

def password_reset(request):
    context = {}
    template_name = 'accounts/password_reset.html'
    form = PasswordResetForm(request.POST or None) # É a mesma coisa que fazer o if request.method
    if form.is_valid(): # se for válido 
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request,template_name,context)

def password_reset_confirm(request,key):
    template_name = 'accounts/password_reset_confirm.html'
    context = {}
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)

#Mostra a página somente se o usuário estiver logado
@login_required
def dashboard(request):
    template_name = 'accounts/dashboard.html'
    context = {}
    # context['enrollments'] = Enrollment.objects.filter(user=request.user) #Pega os dados do usuário atual logado
    return render(request, template_name, context)

@login_required
def edit(request):
    template_name = 'accounts/edit.html'
    context = {}
    if request.method == 'POST':
        form = EditAccountForm(request.POST, request.FILES, instance=request.user) #O request.FILES faz o upload das imagens
        if form.is_valid():
            form.save()
            # form = EditAccountForm(instance=request.user) #Está alterando o usuário atual da sessão
            # context['success'] = True
            messages.success(request, 'Dados alterados com sucesso!')
            return redirect('dashboard')
    else:
        form = EditAccountForm(instance=request.user) # se não for post, formulaŕio vazio
    context['form'] = form
    return render(request, template_name, context) 

@login_required
def edit_password(request):
    template_name = 'accounts/edit_password.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)

@login_required
def addCourse(request):
    template_name = 'accounts/addCourses.html'
    context = {}
    if request.method == 'POST':
        form = AddCoursesForm(request.POST)
        if form.is_valid():
            form.save()
            context['success'] = True
            form = AddCoursesForm()
    else:
        form = AddCoursesForm()
    context['form'] = form
    return render(request, template_name, context)


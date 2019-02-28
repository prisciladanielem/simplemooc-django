from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Course, Enrollment
from .forms import ContactCourse

def index(request):
    courses = Course.objects.all() # carrega todas as informações do banco de dados 
    template_name = 'courses/index.html'
    context = { #dicionario com a variável que será utilizada para substituir os dados do template
        'courses':courses
    }
    return render(request, template_name, context)


# def details(request,pk):
#   course = get_object_or_404(Course,pk=pk) Mostra na url o id do curso ex: curso/1
#   context = {
#       'course':course
#   }
#   template_name = 'courses/details.html'
#   return render(request, template_name, context)

def details(request,slug):
    course = get_object_or_404(Course,slug=slug) #Mostra na url curso/slug
    context = {}
    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid(): #Testa se o form enviado é válido
            context['is_valid'] = True 
            print(form.cleaned_data) #Printa no console os dados enviados válidos
            form.send_mail(course)
            form = ContactCourse()
    else: 
        form = ContactCourse()
    context['course'] = course
    context['form'] = form
    template_name = 'courses/details.html'
    return render(request, template_name, context)

@login_required
def enrollment(request,slug):
    course = get_object_or_404(Course,slug=slug)
    enrollment, created = Enrollment.objects.get_or_create( #faz um filtro.. created retorna um boolean
    user = request.user, #pega o usuário atual
    course = course # e cadastra no curso
    )
    if created: #Se a incrição foi criada
        enrollment.active() #Altera chama a função de ativar o aluno
        messages.success(request, 'Inscrição no curso realizada com sucesso!') #Mensagem informativa
    else:
        messages.info(request, 'Você já está cadastrado nesse curso!')
    return redirect('dashboard')
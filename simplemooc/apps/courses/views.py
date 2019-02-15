from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Course
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



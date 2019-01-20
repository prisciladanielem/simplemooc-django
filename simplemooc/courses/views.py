from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Course

def index(request):
	courses = Course.objects.all() # carrega todas as informações do banco de dados 
	template_name = 'courses/index.html'
	context = { #dicionario com a variável que será utilizada para substituir os dados do template
		'courses':courses
	}
	return render(request, template_name, context)

def details(request,pk):
	course = get_object_or_404(Course,pk=pk)
	context = {
		'course':course
	}
	template_name = 'courses/details.html'
	return render(request, template_name, context)



from django.shortcuts import render
from django.http import HttpResponse

def course(request):
	template_name = 'courses/courses.html'
	return render(request,template_name)


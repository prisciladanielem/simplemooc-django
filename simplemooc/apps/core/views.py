from django.shortcuts import render
from django.http import HttpResponse
from simplemooc.apps.courses.forms import Contact

def home(request):
    return render(request,'home.html')

def contact(request):
    context = {}
    if request.method =='POST':
        form = Contact(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            print(form.cleaned_data)
            form.send_simple_message()
            form = Contact()
    else:
        form = Contact()
    context['form'] = form
    template_name = 'contact.html'

    return  render(request,template_name,context)


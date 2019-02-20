from django.shortcuts import render
from django.http import HttpResponse
from simplemooc.apps.courses.forms import Contact
from django.contrib.auth import get_user_model

User = get_user_model()

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

def base(request):
    accounts = User.objects.all()
    template_name = 'base.html'
    context = {
    'accounts':accounts
    }
    return render(request,template_name,context)

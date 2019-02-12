from django import forms
from django.core.mail import send_mail
from django.conf import settings
import requests
from django.template.loader import render_to_string

from simplemooc.apps.core.mail import send_mail_template, send_mail_contact

class ContactCourse(forms.Form):
    name = forms.CharField(label='Nome',max_length=100)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Mensagem/Dúvida',widget=forms.Textarea)

    def send_mail(self, course):
        subject = '[%s] - Contato' % course
        context = {
            'name':self.cleaned_data['name'],
            'email':self.cleaned_data['email'],
            'message': self.cleaned_data['message']
        }
        template_name = 'courses/contact_email.html'
        send_mail_template(subject, template_name, context, [settings.CONTACT_EMAIL])

class Contact(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    last_name = forms.CharField(label='Sobrenome', max_length=100)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Mensagem', widget=forms.Textarea)

    def send_simple_message(self):
        context = {
        'name':self.cleaned_data['name'],
        'last_name':self.cleaned_data['last_name'],
        'email':self.cleaned_data['email'],
        'message': self.cleaned_data['message']
        }
        subject = '[%s] - Contato' % context['name']
        e_from = "Mailgun Sandbox <postmaster@sandbox20293c5f3f064fef901d3f736ff9359b.mailgun.org>"
        template_name = 'mailgunTeste.html'

        send_mail_contact(e_from, [settings.CONTACT_EMAIL],context, subject, template_name)
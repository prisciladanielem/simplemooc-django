from django.template.loader import render_to_string
from django.template.defaultfilters import striptags
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import requests

#Função para enviar email da página de dúvas sobre os cursos
def send_mail_template(subject, template_name, context, recipient_list, from_email=settings.DEFAULT_FROM_EMAIL, fail_silently=False):
    message_html = render_to_string(template_name, context) #renderiza o template baseado na request
    message_txt = striptags(message_html)
    email = EmailMultiAlternatives(subject =subject, body=message_txt,from_email=from_email,to=recipient_list)
    email.attach_alternative(message_html,"text/html")
    email.send(fail_silently=fail_silently) #Se o envio falhar, manda a exceção ou não

#Função para enviar e-mail da página de contato
def send_mail_contact(c_from, c_to, context, c_subject,c_html):
    c_html = render_to_string(c_html,context)

    MAILGUN_KEY = "81da64d1667a0eb3ff4b4d589bdb65f9-b9c15f4c-722d88ec"
    url = "https://api.mailgun.net/v3/sandbox20293c5f3f064fef901d3f736ff9359b.mailgun.org/messages"
    return requests.post(
        url,
        auth=("api",MAILGUN_KEY),
        data={"from": c_from,
               "to": c_to,
               "subject": c_subject,
               "html": c_html 
               }
            )

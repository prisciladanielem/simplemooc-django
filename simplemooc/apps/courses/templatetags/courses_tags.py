from django import template

from simplemooc.apps.courses.models import Enrollment

register = template.Library() #Para ser uma biblioteca de tags válida, o módulo deve conter uma variável do nível do módulo chamado register que é uma instância de template.Library, na qual todas as tags e filtros são registrados. 

# @register.inclusion_tag('courses/templatetags/my_courses.html') #Converte essa função em uma tag que pode ser usada pelo django e retorna um template
# def my_courses(user):
#     enrollments = Enrollment.objects.filter(user=user) #Pega as inscrições de um usuário
#     context = {
#         'enrollments':enrollments
#     }
#     return context

@register.simple_tag
def load_my_courses(user):
    return Enrollment.objects.filter(user=user) #Retorna as incrições dos usuários
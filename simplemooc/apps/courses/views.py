from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Course, Enrollment, Announcement
from .forms import ContactCourse, CommentForm

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

@login_required
def undo_enrollment(request,slug):
    context = {}
    course = get_object_or_404(Course,slug=slug) # pega o slug
    enrollment = get_object_or_404(
            Enrollment,user = request.user, course = course #Pega as incrições do usuário atual
            )
    if request.method=='POST': # Testa se o usuário quer cancelar a inscrição
        enrollment.delete() # deleta a inscrição
        messages.success(request,'Inscrição cancelada com sucesso!')
        return redirect('dashboard')
    template_name = 'courses/undo_enrollment.html'
    context['enrollment'] = enrollment
    context['course'] = course
    return render(request,template_name, context)

@login_required
def announcements(request,slug):
    course = get_object_or_404(Course,slug=slug)
    if not request.user.is_staff:
        enrollment = get_object_or_404(
            Enrollment,user = request.user, course = course
            )
        if not enrollment.is_approved():
            messages.error(request,'Sua inscrição está pendente!')
            return redirect('dashboard')
    template_name = 'courses/announcements.html'
    context = {}
    context['course'] = course
    context['announcements'] = course.announcements.all() # recebe todos os anuncios do curso (necessário usar o related_name no models)
    return render(request, template_name, context)

def show_announcement(request,slug,pk):
    course = get_object_or_404(Course,slug=slug)
    if not request.user.is_staff:
        enrollment = get_object_or_404(
            Enrollment,user = request.user, course = course
            )
        if not enrollment.is_approved():
            messages.error(request,'Sua inscrição está pendente!')
            return redirect('dashboard')
    announcement = get_object_or_404(course.announcements.all(),pk=pk) #Pega somente os anucios do curso em questão
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False) #Guarda o objeto atual sem salvar no banco de dados
        comment.user = request.user #Pega o usuário atual logado
        comment.announcement = announcement #Pega o anúncio atual que estamos comentando
        comment.save() #Salva o objeto com user, anuncio e Comentário
        form = CommentForm()
        messages.success(request,'Comentário publicado com sucesso!')
    template_name = 'courses/show_announcement.html'
    context = {
        'course':course,
        'announcement': announcement,
        'form':form,
    }
    return render(request,template_name,context)

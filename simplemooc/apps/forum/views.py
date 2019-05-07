from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, View
from django.contrib import messages

from .models import Thread, Reply
from .forms import ReplyForm

# class ForumView(TemplateView):
#     template_name = 'forum/index.html'

# forum_index = ForumView.as_view() # tem a ver com o CBV - pesquisa depois

class ForumView(ListView):

    paginate_by = 2
    template_name = 'forum/index.html'

    def get_queryset(self):
        queryset = Thread.objects.all()
        order = self.request.GET.get('order', '')
        if order == 'views':
            queryset = queryset.order_by('-views')
        elif order == 'answers':
            queryset = queryset.order_by('-answers')
        tag = self.kwargs.get('tag','')
        if tag:
            queryset = queryset.filter(tags__slug__icontains=[tag]) #Filtra as tags
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ForumView, self).get_context_data(**kwargs)
        context['tags'] = Thread.tags.all()
        return context

#**kwargs são parametros nomeados das Urls

class ThreadView(DetailView):

    model = Thread
    template_name = 'forum/thread.html'

    #Contador de visualizações. Conta somente se o usuário logado não for o dono do tópico
    def get(self, request, *args, **kwargs):
        response = super(ThreadView, self).get(request, *args, **kwargs)
        if not self.request.user.is_authenticated or \
            (self.object.author != self.request.user):
            self.object.views = self.object.views + 1
            self.object.save()
        return response

    #DetailView tem somente o métódo get, e nos forms usamos o post
    def get_context_data(self, **kwargs):
        context = super(ThreadView, self).get_context_data(**kwargs)
        context['tags'] = Thread.tags.all()
        context['form'] = ReplyForm(self.request.POST or None)
        return context

    def post(self, request, *args,**kwargs):
        if not self.request.user.is_authenticated:
            messages.error(self.request, 'Para responder ao tópico é necessário estar logado!')
            return redirect(self.request.path)
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        form = context['form']
        if form.is_valid():
            reply = form.save(commit=False)
            reply.thread = self.object
            reply.author = self.request.user
            reply.save()
            messages.success(self.request, 'Resposta enviada com sucesso!')
            context['form'] = ReplyForm() #zera o formulário
        return self.render_to_response(context) #semelhante a função render, mas não passamos template

class ReplyCorrectView(View):

    correct = True

    def get(self, request, pk):
        reply = get_object_or_404(Reply, pk=pk, author=request.user)
        reply.correct = self.correct
        reply.save()
        messages.success(request, 'Resposta atualizada com sucesso')
        return redirect(reply.thread.get_absolute_url())


forum_index = ForumView.as_view() # tem a ver com o CBV - pesquisa depois
thread = ThreadView.as_view()
reply_correct = ReplyCorrectView.as_view()
reply_incorrect = ReplyCorrectView.as_view(correct=False)
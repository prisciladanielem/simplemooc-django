from datetime import datetime

from django.db import models
from django.conf import settings

from taggit.managers import TaggableManager

class Thread(models.Model):
    title = models.CharField('Título', max_length=100)
    slug = models.SlugField('Identificador',max_length=100, unique=True)
    body = models.TextField('Mensagem')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário',
    related_name='threads',
    on_delete=models.CASCADE
    )

    views = models.IntegerField('Visualizações', blank=True, default=0)
    answers = models.IntegerField('Respostas',blank=True, default=0)

    created = models.DateTimeField('Criado em', default=datetime.now)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    tags = TaggableManager()

    def __str__(self):
        return self.title

    @models.permalink   
    def get_absolute_url(self):
        return('thread',(),({'slug':self.slug}))

    class Meta:
        verbose_name='Tópico'
        verbose_name_plural='Tópicos'
        ordering =['-modified']

class Reply(models.Model):
    thread = models.ForeignKey(Thread, verbose_name='Tópico',
    related_name='replies',
    on_delete=models.CASCADE
    )
    reply = models.TextField('Resposta')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário',
    related_name='replies',
    on_delete=models.CASCADE
    )
    correct = models.BooleanField('Correta',blank=True, default=False)
    created = models.DateTimeField('Criado em', default=datetime.now)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.reply[:100]

    class Meta:
        verbose_name='Resposta'
        verbose_name_plural='Respostas'
        ordering=['-correct','created'] # Ordena pela resposta correta e pela data de criação 

#Contador das respostas, soma um sempre que uma nova resposta for adicionada
def post_save_reply(created,instance,**kwargs):
    if created:
        instance.thread.answers = instance.thread.replies.count()
        instance.thread.save()

#Contador das repostas, mas sempre que uma resposta for deletada, tira um
def post_delete_reply(created,instance,**kwargs):
    instance.thread.answers = instance.thread.replies.count()
    instance.thread.save()
    if instance.correct:
        instance.thread.replies.exclude(pk=instance.pk).update(
            correct=False
        )

#Envia o sinal 
models.signals.post_save.connect(
    post_save_reply,
    sender=Reply, #Envia o sinal somente quando o model reply ser chamado
    dispatch_uid='post_save_reply'
    )

models.signals.post_delete.connect(
    post_delete_reply,
    sender=Reply, #Envia o sinal somente quando o model reply ser chamado
    dispatch_uid='post_delete_reply'
    )


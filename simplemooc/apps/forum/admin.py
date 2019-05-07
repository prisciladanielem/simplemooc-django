from django.contrib import admin

from .models import Thread, Reply

class ThreadAdmin(admin.ModelAdmin):
    list_display = ['title','slug','author','created','modified']
    search_fields = ['title','author__email','body'] #Dois underlines faz o join com a tabela de user e pega o email
    prepopulated_fields ={'slug':('title',)}

class ReplyAdmin(admin.ModelAdmin):
    list_display = ['thread','author','correct','created','modified']
    search_fields = ['thread__title','reply','author__email']


admin.site.register(Thread, ThreadAdmin)
admin.site.register(Reply,  ReplyAdmin)
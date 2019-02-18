from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['username','name', 'email', 'data_joined'] #Mostra esses campos no admin
    search_fields = ['name','username','email'] #Exibe uma barra de pesquisa, onde é possível pesquisar por esses campos

admin.site.register(User, UserAdmin)

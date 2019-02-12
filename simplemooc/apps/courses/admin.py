from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'start_date','created_at'] #Mostra esses campos no admin
	search_fields = ['name','slug'] #Exibe uma barra de pesquisa, onde é possível pesquisar por esses campos
	prepopulated_fields ={'slug':('name',)}

admin.site.register(Course, CourseAdmin)



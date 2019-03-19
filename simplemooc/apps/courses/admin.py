from django.contrib import admin
from .models import Course, Enrollment, Announcement, Comment, Lesson, Material

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date','created_at'] #Mostra esses campos no admin
    search_fields = ['name','slug'] #Exibe uma barra de pesquisa, onde é possível pesquisar por esses campos
    prepopulated_fields ={'slug':('name',)}

#formset conjunto de formulário que junta um ou mais models. Criar o class com o TabularInline  ou StackedInline (formas de visualização)e chamar dentro do outro admin
class MaterialInlineAdmin(admin.StackedInline):
    model = Material

class LessonAdmin(admin.ModelAdmin):
    list_display = ['name','number','course','release_date']
    search_fields = ['name','description']
    list_filter = ['created_at'] #Filtro lateral
    inlines = [
        MaterialInlineAdmin
    ]

admin.site.register(Course, CourseAdmin)
admin.site.register([Enrollment, Announcement, Comment, Material])
admin.site.register(Lesson, LessonAdmin)
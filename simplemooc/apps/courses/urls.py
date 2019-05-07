from django.urls import path
from simplemooc.apps.courses.views import index,details, enrollment,undo_enrollment,announcements, show_announcement, lessons,lesson, material

urlpatterns = [
    path('',index, name="index"),
    path('<str:slug>/',details, name="details"),
    #path('<str:pk>',details, name="details"
    path('<str:slug>/incricao',enrollment, name="enrollment"),
    path('<str:slug>/cancelar-inscricao',undo_enrollment, name="undo_enrollment"),
    path('<str:slug>/anuncios',announcements, name="announcements"),
    path('<str:slug>/aulas',lessons, name="lessons"),
    path('<str:slug>/aulas/<int:pk>/',lesson, name="lesson"),
    path('<str:slug>/materiais/<int:pk>/',material, name="material"),
    path('<str:slug>/anuncios/<int:pk>/',show_announcement, name="show_announcement"),

]
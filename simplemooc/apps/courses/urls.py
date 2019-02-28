from django.urls import path
from simplemooc.apps.courses.views import index,details, enrollment

urlpatterns = [
    path('',index, name="index"),
    path('<str:slug>/',details, name="details"),
    #path('<str:pk>',details, name="details"),
    path('<str:slug>/incricao',enrollment, name="enrollment"),
]
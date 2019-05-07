from django.urls import path
from simplemooc.apps.forum.views import forum_index,thread, reply_correct, reply_incorrect

urlpatterns = [
    path('',forum_index, name="forum_index"),
    path('tag/<str:tag>/',forum_index, name="forum_index_tagged"),
    path('respostas/<int:pk>/correta/',reply_correct, name="reply_correct"),
    path('respostas/<int:pk>/incorreta/',reply_incorrect, name="reply_incorrect"),
    path('<str:slug>/',thread, name="thread"),
]
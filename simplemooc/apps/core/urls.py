from django.urls import path
from simplemooc.apps.core.views import home, contact

urlpatterns = [
    path('',home, name="home"),
    path('contato/',contact, name="contact"),
]
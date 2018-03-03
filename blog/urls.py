from django.urls import path
from . import views

urlpatterns = [
    path('', views.firstWord, name='firstWord'),
]
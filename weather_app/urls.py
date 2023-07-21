from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('search/', views.search_results, name='search'),
    path('clear/', views.clearing, name='clear'),
    path('change_lang/', views.change_lang, name='change_lang')
]
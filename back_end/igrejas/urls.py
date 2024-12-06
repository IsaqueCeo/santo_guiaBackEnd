from django.urls import path
from . import views

app_name = 'pesquisa'

urlpatterns = [
    path('pesquisar/', views.pesquisar_eventos, name='pesquisar_eventos'),
]

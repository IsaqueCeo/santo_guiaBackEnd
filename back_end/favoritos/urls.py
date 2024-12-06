from django.urls import path
from . import views

app_name = 'favoritos'

urlpatterns = [
    path('adicionar_favorito/<int:evento_id>/', views.adicionar_favorito, name='adicionar_favorito'),
    path('remover_favorito/<int:evento_id>/', views.remover_favorito, name='remover_favorito'),
]

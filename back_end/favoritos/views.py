# Em favoritos/views.py
from django.shortcuts import redirect
from .models import Evento, Favorito  # Importe o Evento corretamente

from django.contrib.auth.decorators import login_required

@login_required
def adicionar_favorito(request, evento_id):
    evento = Evento.objects.get(id=evento_id)
    favorito, created = Favorito.objects.get_or_create(usuario=request.user, evento=evento)
    return redirect('pesquisa:pesquisar_eventos')  # Redireciona de volta para a página de pesquisa

@login_required
def remover_favorito(request, evento_id):
    evento = Evento.objects.get(id=evento_id)
    Favorito.objects.filter(usuario=request.user, evento=evento).delete()
    return redirect('pesquisa:pesquisar_eventos')

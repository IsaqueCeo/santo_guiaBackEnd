from django.shortcuts import render
from .models import Evento, Igreja
from django.db.models import Q

def pesquisar_eventos(request):
    eventos = Evento.objects.all()
    
    # Filtros de pesquisa
    if 'tipo' in request.GET:
        tipo = request.GET['tipo']
        eventos = eventos.filter(tipo=tipo)
    
    if 'data_inicio' in request.GET and 'data_fim' in request.GET:
        data_inicio = request.GET['data_inicio']
        data_fim = request.GET['data_fim']
        eventos = eventos.filter(horario__range=[data_inicio, data_fim])

    if 'localizacao' in request.GET:
        localizacao = request.GET['localizacao']
        eventos = eventos.filter(igreja__endereco__icontains=localizacao)

    return render(request, 'pesquisa/resultados.html', {'eventos': eventos})

def mapa_eventos(request):
             igrejas = Igreja.objects.all()
             return render(request, 'mapa.html', {'igrejas': igrejas})

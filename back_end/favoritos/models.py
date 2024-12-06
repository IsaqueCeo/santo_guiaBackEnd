from django.conf import settings
from django.db import models

class Favorito(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favoritos_favorito_set')
    evento = models.ForeignKey('igrejas.Evento', on_delete=models.CASCADE, related_name='favoritos_favorito_set')  # Aqui estamos referenciando corretamente 'Evento'

    def __str__(self):
        return f"{self.usuario.username} - {self.evento.tipo} em {self.evento.igreja.nome}"

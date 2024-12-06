from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission
import re, random

class Perfil(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField("Telefone", max_length=11)
    nome = models.CharField("Nome Completo", max_length=100)
    concorda_termos = models.BooleanField(default=False)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
    
    def gerar_username(self):
        email = self.email
        if '@' in email:
            base_username = email.split('@')[0]
        else:
            base_username = email
        
        while True:
            numeros_aleatorios = ''.join(random.choices('0123456789', k=4))
            username = f"{base_username}{numeros_aleatorios}"
            if not Perfil.objects.filter(username=username).exists():
                break
        
        return username
    
    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.gerar_username()
        super().save(*args, **kwargs)

    
    class Meta:
        verbose_name = "Perfil de Login"
        verbose_name_plural = "Perfis de Login"  


class Igreja(models.Model):
    nome = models.CharField(max_length=100)
    rua = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return self.nome
    


class Evento(models.Model):
    TIPOS_EVENTO = [
        ('missa', 'Missa'),
        ('adoracao', 'Adoração'),
        ('confissao', 'Confissão'),
    ]
    igreja = models.ForeignKey(Igreja, on_delete=models.CASCADE)
    tipo = models.CharField(choices=TIPOS_EVENTO, max_length=50)
    horario = models.DateTimeField()
    descricao = models.TextField()

    def __str__(self):
        return f"{self.tipo} - {self.igreja.nome} ({self.horario})"
    
# class Usuario(models.Model):
#     user = models.ForeignKey(Perfil, on_delete=models.CASCADE)
#     evento_favorito = 
#     igreja_favorita =
#     ...
from django.contrib import admin
from .models import Igreja, Evento, Favorito
from .models import Usuario

admin.site.register(Igreja)
admin.site.register(Evento)
admin.site.register(Favorito)


# Personalizando a interface do admin para o modelo Usuario
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'data_nascimento', 'telefone', 'endereco', 'is_active')
    list_filter = ('is_active', 'is_staff', 'date_joined')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

    # Configuração de campos do formulário no admin
    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'first_name', 'last_name', 'email')
        }),
        ('Informações adicionais', {
            'fields': ('data_nascimento', 'telefone', 'endereco')
        }),
        ('Permissões', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')
        }),
        ('Informações adicionais', {
            'classes': ('wide',),
            'fields': ('data_nascimento', 'telefone', 'endereco')
        }),
    )

# Registrando o modelo Usuario no painel de administração
admin.site.register(Usuario, UsuarioAdmin)

from django.contrib import admin
from biblioteca_jogos.website.models import Pessoa

# Register your models here.

class PessoaModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf')
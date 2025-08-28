from django.contrib import admin
from biblioteca_jogos.website.models import Pessoa, Slideshow

# Register your models here.

class PessoaModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf', 'telefone', 'data_nascimento', 'criado_em')
    list_filter = ('criado_em', 'atualizado_em')
    search_fields = ('nome', 'email', 'cpf', 'telefone')
    ordering = ('nome',)
    readonly_fields = ('criado_em', 'atualizado_em')
    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('nome', 'email', 'cpf', 'data_nascimento', 'telefone', 'endereco')
        }),
        ('Timestamps', {
            'fields': ('criado_em', 'atualizado_em'),
            'classes': ('collapse',),
        }),
    )

class SlideshowModelAdmin(admin.ModelAdmin):
    list_display = ['titulo','imagem','alt','descricao',]
    search_fields = ('titulo',)

admin.site.register(Pessoa, PessoaModelAdmin)


admin.site.register(Slideshow, SlideshowModelAdmin)
from django.contrib import admin
from . models import Fotografia, Categoria

class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id','nome','descricao','categoria', 'publicada')
    list_filter = ('categoria',)
    list_display_links = ('id','nome')
    list_editable = ('publicada',)

# Register your models here.
admin.site.register(Fotografia, ListandoFotografias)
admin.site.register(Categoria)
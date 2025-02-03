from django.contrib import admin
from .models import (
    TipoLead,
    Programa,
    Momento,
    Submomento,
    Respuesta,
    Documento
)


@admin.register(TipoLead)
class TipoLeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'tipo_lead')
    list_filter = ('tipo_lead',)


@admin.register(Momento)
class MomentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'programa', 'programa__tipo_lead')
    list_filter = ('programa',)


@admin.register(Submomento)
class SubmomentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'momento', 'programa', 'tipo_lead')
    list_filter = ('momento', 'programa', 'tipo_lead')


@admin.register(Respuesta)
class RespuestaAdmin(admin.ModelAdmin):
    list_display = ('id', 'contenido', 'prioridad', 'submomento')
    list_filter = ('submomento',)


# # @admin.register(Historial)
# # class HistorialAdmin(admin.ModelAdmin):
# #     readonly_fields = ('momento', 'submomento', 'respuesta', 'timestamp')  # Campos de solo lectura
# #     list_display = ('momento', 'submomento', 'respuesta', 'timestamp')  # Para mostrar en la lista del admin

# @admin.register(Documento)
# class DocumentoAdmin(admin.ModelAdmin):
#     list_display = ('id', 'nombre', 'archivo', 'palabras_clave')
#     search_fields = ('palabras_clave',)


# admin.site.register(TipoLead)
# admin.site.register(Programa)
# admin.site.register(Momento)
# admin.site.register(Submomento)
# admin.site.register(Respuesta)
# admin.site.register(Documento)

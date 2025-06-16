from django.db.models import Q

from rest_framework import viewsets


from chatbot_app.models import (
    TipoLead,
    Programa,
    Momento,
    Submomento,
    Respuesta,
    Documento,
)
from chatbot_app.serializers import (
    TipoLeadSerializer,
    ProgramaSerializer,
    MomentoSerializer,
    SubmomentoSerializer,
    RespuestaSerializer,
    DocumentoSerializer,
)


# Api classes
class TipoLeadViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TipoLeadSerializer
    queryset = TipoLead.objects.all().order_by("id")


class ProgramaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer

    def get_queryset(self):

        queryset = Programa.objects.all()

        tipo_lead_id = self.request.GET.get("tipo_lead_id")
        if tipo_lead_id:
            return queryset.filter(tipo_lead_id=tipo_lead_id)
        return queryset


class MomentoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Momento.objects.all()
    serializer_class = MomentoSerializer

    def get_queryset(self):

        queryset = Momento.objects.all()

        programa_id = self.request.GET.get("programa_id")
        if programa_id:
            return queryset.filter(programa_id=programa_id)
        return queryset


class SubmomentoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Submomento.objects.all()
    serializer_class = SubmomentoSerializer

    def get_queryset(self):

        queryset = Submomento.objects.all()

        momento_id = self.request.GET.get("momento_id")
        if momento_id:
            return queryset.filter(momento_id=momento_id)
        return queryset


class RespuestaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer

    def get_queryset(self):

        queryset = Respuesta.objects.all().order_by("prioridad")

        submomento_id = self.request.GET.get("submomento_id")
        if submomento_id:
            return queryset.filter(submomento_id=submomento_id)

        return queryset


class DocumentoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DocumentoSerializer

    def get_queryset(self):

        queryset = Documento.objects.all()

        tags = self.request.GET.get("tags")
        
        # No return data if no tags
        if not tags:
            return queryset.none()
        
        # Filetr by tags
        if tags:
            tags = tags.split(",")
            query = Q()
            for tag in tags:
                query |= Q(palabras_clave__icontains=f'"value":"{tag}"')
            queryset = queryset.filter(query)

        return queryset

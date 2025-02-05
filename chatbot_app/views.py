
from rest_framework import viewsets

from .models import TipoLead, Programa, Momento, Submomento, Respuesta, Documento
from .serializer import (
    TipoLeadSerializer, ProgramaSerializer, MomentoSerializer,
    SubmomentoSerializer, RespuestaSerializer, DocumentoSerializer
)


class TipoLeadViewSet(viewsets.ModelViewSet):
    serializer_class = TipoLeadSerializer
    queryset = TipoLead.objects.all()


class ProgramaViewSet(viewsets.ModelViewSet):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer
    
    def get_queryset(self):
        
        queryset = Programa.objects.all()
        
        tipo_lead_id = self.request.GET.get('tipo_lead_id')
        if tipo_lead_id:
            return queryset.filter(tipo_lead_id=tipo_lead_id)
        return queryset


class MomentoViewSet(viewsets.ModelViewSet):
    queryset = Momento.objects.all()
    serializer_class = MomentoSerializer
    
    def get_queryset(self):
        
        queryset = Momento.objects.all()
        
        programa_id = self.request.GET.get('programa_id')
        if programa_id:
            return queryset.filter(programa_id=programa_id)
        return queryset


class SubmomentoViewSet(viewsets.ModelViewSet):
    queryset = Submomento.objects.all()
    serializer_class = SubmomentoSerializer


class RespuestaViewSet(viewsets.ModelViewSet):
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer


class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

# # def get_tipo_lead(request):
# #     tipos = list(TipoLead.objects.values('id', 'nombre'))
# #     return JsonResponse({'tipos': tipos})


# class TipoLeadViewSet(ViewSet):
#     def list(self, request):
#         tipos = list(TipoLead.objects.values('id', 'nombre'))
#         return Response({'tipos': tipos})


# # @csrf_exempt
# # def get_programa(request):
# #     print("-----> programa")
# #     if request.method == 'GET':
# #         tipo_lead_id = request.GET.get('tipo_lead_id')
# #         programas = Programa.objects.filter(tipo_lead_id=tipo_lead_id)
# #         print("----->", programas)
# #         data = [{"id": p.id, "nombre": p.nombre} for p in programas]
# #         return JsonResponse({"programas": data})

# class ProgramaViewSet(ViewSet):
#     def list(self, request):
#         tipo_lead_id = request.GET.get('tipo_lead_id')
#         programas = Programa.objects.filter(tipo_lead_id=tipo_lead_id)
#         data = [{"id": p.id, "nombre": p.nombre} for p in programas]
#         return Response({"programas": data})

# # @csrf_exempt
# # def get_momento(request):
# #     print("-----> momento")
# #     if request.method == 'GET':
# #         programa_id = request.GET.get('programa_id')
# #         print("----->", programa_id)
# #         momentos = Momento.objects.filter(programa_id=programa_id)
# #         print("----->", momentos)
# #         data = [{"id": m.id, "nombre": m.nombre} for m in momentos]
# #         return JsonResponse({"momentos": data})


# class MomentoViewSet(ViewSet):
#     def list(self, request):
#         programa_id = request.GET.get('programa_id')
#         momentos = Momento.objects.filter(programa_id=programa_id)
#         data = [{"id": m.id, "nombre": m.nombre} for m in momentos]
#         return Response({"momentos": data})

# # def get_submomento(request):
# #     momento_id = request.GET.get('momento_id')
# #     submomentos = Submomento.objects.filter(
# #         momento_id=momento_id).values('id', 'nombre')
# #     return JsonResponse({'submomentos': list(submomentos)})


# class SubmomentoViewSet(ViewSet):
#     def list(self, request):
#         momento_id = request.GET.get('momento_id')
#         submomentos = Submomento.objects.filter(
#             momento_id=momento_id).values('id', 'nombre')
#         return Response({'submomentos': list(submomentos)})

# # def get_respuesta(request):
# #     submomento_id = request.GET.get('submomento_id')
# #     respuestas = Respuesta.objects.filter(
# #         submomento_id=submomento_id).values('id', 'contenido')
# #     return JsonResponse({'respuestas': list(respuestas)})


# class RespuestaViewSet(ViewSet):
#     def list(self, request):
#         submomento_id = request.GET.get('submomento_id')
#         respuestas = Respuesta.objects.filter(
#             submomento_id=submomento_id).values('id', 'contenido')
#         return Response({'respuestas': list(respuestas)})
# # def get_historial(request):
# #     historial = Historial.objects.all().values(
# #         'momento__nombre', 'submomento__nombre', 'respuesta__contenido', 'timestamp'
# #     )
# #     return JsonResponse({'historial': list(historial)})


# # def nueva_conversacion(request):
# #     # Reinicia lógica de la conversación
# #     return JsonResponse({'status': 'Nueva conversación iniciada'})
# # class ConversacionViewSet(ViewSet):
# #     def create(self, request):
# #         # Reinicia lógica de la conversación
# #         return Response({'status': 'Nueva conversación iniciada'})

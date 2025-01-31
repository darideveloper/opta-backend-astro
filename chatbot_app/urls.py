from django.urls import path, include

from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from chatbot_app import views

router = routers.DefaultRouter()


router.register(r'tipolead', views.TipoLeadViewSet, 'tipolead')
router.register(r'programa', views.ProgramaViewSet, 'programa')
router.register(r'momento',  views.MomentoViewSet, 'momento')
router.register(r'submomento', views.SubmomentoViewSet, 'submomento')
router.register(r'respuesta', views.RespuestaViewSet, 'respuesta')
router.register(r'documento', views.DocumentoViewSet, 'documento')

urlpatterns = [


    path('api/', include(router.urls)),
    path('docs/', include_docs_urls(title="Chat Assistent API")),

]

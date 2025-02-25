from rest_framework import serializers
from .models import TipoLead, Programa, Momento, Submomento, Respuesta, Documento


class TipoLeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoLead
        fields = '__all__'


class ProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programa
        fields = '__all__'


class MomentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Momento
        fields = '__all__'


class SubmomentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submomento
        fields = '__all__'


class RespuestaSerializer(serializers.ModelSerializer):
    
    documento_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Respuesta
        fields = '__all__'
        
    def get_documento_url(self, obj):
        return obj.documento.archivo.url if obj.documento else None


class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = '__all__'

from rest_framework import serializers
from .models import TipoLead, Programa, Momento, Submomento, Respuesta, Documento


class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = '__all__'


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
    
    documento = DocumentoSerializer()
    
    class Meta:
        model = Respuesta
        fields = '__all__'


class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        exclude = ['palabras_clave']

#Contruccion serializadores
from rest_framework import serializers
from Cuenta.models import *

class serializador_Perfil (serializers.ModelSerializer):
    class Meta:
        model=Perfil
        fields = '__all__'
class serializador_TipoCarteraAhorro (serializers.ModelSerializer):
    class Meta:
        model=TipoCarteraAhorro
        fields = '__all__'
class serializador_CarteraAhorro (serializers.ModelSerializer):
    class Meta:
        model=CarteraAhorro
        fields = '__all__'
class serializador_Ingresos (serializers.ModelSerializer):
    class Meta:
        model=Ingresos
        fields = '__all__'
class serializador_TipoEgreso (serializers.ModelSerializer):
    class Meta:
        model=TipoEgreso
        fields = '__all__'
class serializador_Egreso (serializers.ModelSerializer):
    class Meta:
        model=Egreso
        fields = '__all__'
from django.shortcuts import render

# Creamos las APIS.
from rest_framework import viewsets
from Cuenta.serializers import *

class PerfilAPI(viewsets.ModelViewSet):
    serializer_class= serializador_Perfil
    queryset = Perfil.objects.all()

class TipoCarteraAhorroAPI(viewsets.ModelViewSet):
    serializer_class= serializador_TipoCarteraAhorro
    queryset = TipoCarteraAhorro.objects.all()

class CarteraAhorroAPI(viewsets.ModelViewSet):
    serializer_class= serializador_CarteraAhorro
    queryset = CarteraAhorro.objects.all()

class IngresosAPI(viewsets.ModelViewSet):
    serializer_class= serializador_Ingresos
    queryset = Ingresos.objects.all()

class TipoEgresoAhorroAPI(viewsets.ModelViewSet):
    serializer_class= serializador_TipoEgreso
    queryset = TipoEgreso.objects.all()

class EgresosAPI(viewsets.ModelViewSet):
    serializer_class= serializador_Egreso
    queryset = Egreso.objects.all()




#Almacenar todas las direcciones locales de la aplicación

from django.urls import path,include
from django.urls.resolvers import URLPattern
from rest_framework.routers import DefaultRouter
from Cuenta.views import *

router=DefaultRouter()
router.register('login',PerfilAPI)
router.register('CarteraAhorro',CarteraAhorroAPI)
router.register('Ingreso',IngresosAPI)
router.register('Egreso',EgresosAPI)




urlpatterns=[
    path("api/", include(router.urls))
]
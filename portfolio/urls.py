from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import api # desde la raiz de la app importamos el archiv api.py

router = DefaultRouter()
router.register('categorias', api.CategoriaViewSet, basename='categoria')
router.register('tecnologias', api.TecnologiaViewSet, basename='tecnologia')

urlpatterns = [
    path('', include(router.urls))
]
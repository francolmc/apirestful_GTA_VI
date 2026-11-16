from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Proyecto
from .serializers import ProyectoSerializer

# Create your views here.
# GET - /api/v1/proyectos (obtener todos los proyectos)
# POST - /api/v1/proyectos (crear un proyecto)
def proyectos_api(request):
    pass
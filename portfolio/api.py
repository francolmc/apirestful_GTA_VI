from rest_framework import filters, viewsets, generics, permissions
from .models import Categoria, Tecnologia
from .serializers import CategoriaSerializer, TecnologiaSerializer, RegistroSerializer, UsuarioSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.order_by('nombre')
    serializer_class = CategoriaSerializer

class TecnologiaViewSet(viewsets.ModelViewSet):
    queryset = Tecnologia.objects.order_by('nombre')
    serializer_class = TecnologiaSerializer

class RegistroView(generics.CreateAPIView):
    serializer_class = RegistroSerializer
    permission_classes = [permissions.AllowAny]

class PerfilView(generics.RetrieveAPIView):
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
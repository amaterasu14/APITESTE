from rest_framework import viewsets
from apifaculdade.models import Senha
from apifaculdade.serializers import SenhaSerializer

class SenhaViewSet(viewsets.ModelViewSet):
  queryset = Senha.objects.all()
  serializer_class = SenhaSerializer

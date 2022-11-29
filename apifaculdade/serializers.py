from rest_framework import serializers
from apifaculdade.models import Senha

class SenhaSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Senha
    fields = '__all__'
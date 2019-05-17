from rest_framework import serializers
from .models import Cliente, Modality

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'nome', 'endereco', 'idade')

class ModalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Modality
        fields = ('id', 'description', 'updatedOnVersion')

   
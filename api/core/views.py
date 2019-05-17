from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente, Modality
from .serializers import ClienteSerializer, ModalitySerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ModalityViewSet(viewsets.ModelViewSet):
    queryset = Modality.objects.all()
    serializer_class = ModalitySerializer

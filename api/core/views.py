from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente, Modality, AnatomicalRegion, AnatomyImage, Answer, Assignment, Question
from .serializers import ClienteSerializer, ModalitySerializer, AnatomicalRegionSerializer, AnatomyImageSerializer, AnswerSerializer, AssignmentSerializer, QuestionSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ModalityViewSet(viewsets.ModelViewSet):
    queryset = Modality.objects.all()
    serializer_class = ModalitySerializer

class AnatomicalRegionViewSet(viewsets.ModelViewSet):
    queryset = AnatomicalRegion.objects.all()
    serializer_class = AnatomicalRegionSerializer

class AnatomyImageViewSet(viewsets.ModelViewSet):
    queryset = AnatomyImage.objects.all()
    serializer_class = AnatomyImageSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

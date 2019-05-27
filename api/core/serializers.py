from rest_framework import serializers
from .models import Cliente, Modality, AnatomicalRegion, AnatomyImage, Answer, Assignment, Question

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'nome', 'endereco', 'idade')

class ModalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Modality
        fields = ('id', 'description', 'updatedOnVersion')

class AnatomicalRegionSerializer(serializers.ModelSerializer):

    modalityFk = serializers.HyperlinkedIdentityField(
        view_name='modality-detail', format='html')

    class Meta:
        model = AnatomicalRegion
        fields = ('id', 'description', 'modalityFk', )


class AssignmentSerializer(serializers.ModelSerializer):

    anatomicalRegionFk = serializers.HyperlinkedIdentityField(
        view_name='anatomicalregion-detail', format='html')

    class Meta:
        model = Assignment
        fields = ('id', 'description', 'anatomicalRegionFk',)


class AnatomyImageSerializer(serializers.ModelSerializer):

    assignmentFk = serializers.HyperlinkedIdentityField(
        view_name='assignment-detail', format='html')

    class Meta:
        model = AnatomyImage
        fields = ('id', 'imagePath', 'assignmentFk', )


class QuestionSerializer(serializers.ModelSerializer):

    assignmentFk = serializers.HyperlinkedIdentityField(
        view_name='assignment-detail', format='html')

    class Meta:
        model = Question
        fields = ('id', 'description', 'assignmentFk', )


class AnswerSerializer(serializers.ModelSerializer):

    questionFk = serializers.HyperlinkedIdentityField(
        view_name='question-detail', format='html')

    class Meta:
        model = Answer
        fields = ('id', 'description', 'questionFk', 'isCorrectAnswer', )
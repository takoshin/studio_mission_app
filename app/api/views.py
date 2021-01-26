from rest_framework import generics

from polls.models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer


class QuestionAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceAPIView(generics.ListAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
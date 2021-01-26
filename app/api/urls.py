from .views import QuestionAPIView, ChoiceAPIView
from django.urls import path


urlpatterns = [
    path('question', QuestionAPIView.as_view()),
    path('choice', ChoiceAPIView.as_view()),
]
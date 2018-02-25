from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import generics

#get models
from ..models import Question, Choice

#get serializers
from .serializers import  QuestionListSerializer


class QuestionListAPIView(generics.ListCreateAPIView):
    """
     Lists all or creates a new question instance
    """
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer


    def post(self, request, format=None):
        """
        nothing required for lab 5
        """
        pass

    def put(self, request, format=None):
        """
        nothing required for lab 5
        """
        pass

    def delete(self, request, format=None):
        """
        nothing required for lab 5
        """
        pass

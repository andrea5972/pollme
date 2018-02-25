"""
polls.api.urls conf
"""
from django.urls import path

from .views import QuestionListAPIView


app_name = "polls_api"
urlpatterns = [
    path('', QuestionListAPIView.as_view(), name='questions_list'),
]

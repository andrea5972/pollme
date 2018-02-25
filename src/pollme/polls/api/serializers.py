
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import  SerializerMethodField
from rest_framework import serializers

from ..models import Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('choice_text', 'votes')
    """
    Serializes the Choice model
    """

class QuestionListSerializer(serializers.ModelSerializer):
    """
    This serializer serializes the Question model
    Return-nested-serializer-in-serializer-method-field
    """
    choices = serializers.SerializerMethodField(source= 'get_choices')

    class Meta:
        model = Question
        fields =('id', 'text', 'pub_date', 'choices')


    def get_choices(self, obj):
        """
        Accessor to the related objects manager on the reverse side of a
        many-to-one relation with choice_set
        Retuns: the ChoiceSerializer; all the related data
        """

        choice = obj.choice_set.all()
        return ChoiceSerializer(choice, many=True).data


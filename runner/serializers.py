from django.db import models
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
import os

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('__all__')

    @staticmethod
    def create(validated_data):
        users = User.objects.all()
        for user in users:
            if not os.path.exists('CodeDatas/Users/{}/{}'.format(user.username, validated_data.get('que_id'))):
                os.makedirs('CodeDatas/Users/{}/{}'.format(user.username, validated_data.get('que_id')))
        instance = Question.objects.create(**validated_data)
        return instance

class TestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCases
        fields = ('__all__')

    @staticmethod
    def create(validated_data):
        print(validated_data.get('questionID'))
        quesID = validated_data.get('questionID')
        ques = Question.objects.get(que_id=quesID.que_id)
        ques.no_of_tc = ques.no_of_tc + 1
        ques.save()
        instance = TestCases.objects.create(**validated_data)
        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'pk')

    @staticmethod
    def create(validated_data):
        os.makedirs('CodeDatas/Users/{}'.format(validated_data.get('username')), 0o755)
        os.chdir('CodeDatas/Users/{}'.format(validated_data.get('username')))
        questions = Question.objects.all()
        for ques in questions:
            os.makedirs('{}'.format(ques.que_id))
        instance = User.objects.create_user(**validated_data)
        return instance

class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = ('__all__')

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        models = Submission
        fields = ('__all__')
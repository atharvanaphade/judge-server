from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.mixins import *
from rest_framework.generics import *


# Create your views here.

class UserCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class QuestionListView(ListModelMixin, GenericAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class QuestionListCreateView(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminUser]

class QuestionDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminUser]

class TestCaseListCreateView(ListCreateAPIView):
    queryset = TestCases.objects.all()
    serializer_class = TestCaseSerializer
    permission_classes = [IsAdminUser]

class TestCaseDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = TestCases.objects.all()
    serializer_class = TestCaseSerializer
    permission_classes = [IsAdminUser]
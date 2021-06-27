from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('user/', UserCreateView.as_view()),
    path('user/<int:pk>', UserDetailsView.as_view()),
    path('questions/', QuestionListView.as_view()),
    path('question_add/', QuestionListCreateView.as_view()),
    path('question_edit/<int:pk>', QuestionDetailsView.as_view()),
    path('testcase_add/', TestCaseListCreateView.as_view()),
    path('testcase_edit/<int:pk>', TestCaseDetailsView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

SubmissionStates = (
   ('69',  'JUDGING'),
    ('0',  'AC'),
   ('-1',  'WA'),
  ('129',  'CTE'),
  ('135',  'MLE'),
   ('42',  'TLE'),
)

QuestionTypes = (
    ('RE','Regular'),
    ('CA','Constructive'),
)

class Question(models.Model):
    que_id       = models.CharField(max_length=32)
    type         = models.CharField(max_length=32, choices=QuestionTypes)
    no_of_tc     = models.IntegerField(default=1)

    def __str__(self):
        return self.que_id

class TestCases(models.Model):
    questionID   = models.ForeignKey(Question, on_delete=models.CASCADE)
    input        = models.TextField(default='')
    output       = models.TextField(default='')
    time_limit   = models.IntegerField(default=1)
    memory_limit = models.IntegerField(default=64)

    def __str__(self):
        return ("TestCase for Question {}".format(self.questionID.que_id))

class Submission(models.Model):
    que_id       = models.ForeignKey(Question, on_delete=models.CASCADE)
    userID       = models.ForeignKey(User, on_delete=models.CASCADE)
    status       = models.CharField(max_length=10, choices=SubmissionStates, default=SubmissionStates[0])
    created_at   = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return ("{}'s Submisison for {}".format(self.userID.username, self.que_id.que_id))

class Code(models.Model):
    sub_id       = models.OneToOneField(Submission, on_delete=models.CASCADE)
    buffer       = models.FileField(max_length=256, upload_to="CodeDatas/UnReferenced/Codefiles")
    language     = models.CharField(max_length=10, default='')
    file_ext     = models.CharField(max_length=10, default='')

    def __str__(self):
        return ("{}'s code for {}".format(self.sub_id.userID.username, self.sub_id.que_id.que_id))
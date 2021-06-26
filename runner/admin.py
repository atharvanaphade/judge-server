from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Code)
admin.site.register(Submission)
admin.site.register(Question)
admin.site.register(TestCases)

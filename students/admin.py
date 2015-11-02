from django.contrib import admin
from students.models.student import Student
from students.models.group import Groups
from students.models.examination import Exam

#models tuple
models = (Student, Groups, Exam)
#register models
admin.site.register(models)

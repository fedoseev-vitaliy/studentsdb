from django.contrib import admin
from students.models.student import Student
from students.models.group import Groups

#models tuple
models = (Student, Groups)
#register models
admin.site.register(models)

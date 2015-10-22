from django.contrib import admin
from students.models import Student, Groups

#models tuple
models = (Student, Groups)
#register models
admin.site.register(models)

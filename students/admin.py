# -*- coding: utf-8 -*-
from django.contrib import admin
from students.models.student import Student
from students.models.group import Groups
from students.models.examination import Exam
from django.core.urlresolvers import reverse

# additional action to copy selected students
def copy_students(model_admin, request, queryset):
    for item in queryset:
        Student(first_name=item.first_name + '(copy)',
                last_name=item.last_name + '(copy)',
                birth_day=item.birth_day,
                ticket=item.ticket,
                student_group=item.student_group).save()
copy_students.short_description = u'Копіювати вибрані Студенти'

#studnet admin class
class StudentAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'ticket', 'student_group']
    list_display_links = ['last_name', 'first_name']
    list_editable = ['student_group']
    ordering = ['last_name']
    list_filter = ['student_group']
    list_per_page = 10
    search_fields = ['last_name', 'first_name', 'middle_name', 'ticket', 'notes']
    actions=[copy_students,]
    
    def view_on_site(self, obj):
        return reverse('students_edit', kwargs={'sid':obj.id})


# additional action to copy selected students
def copy_groups(model_admin, request, queryset):
    for item in queryset:
        Groups(title=item.title + '(copy)',).save()
copy_groups.short_description = u'Копіювати вибрані Групи'

#studnet admin class
class GroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'leader']
    list_display_links = ['title']
    list_editable = ['leader']
    ordering = ['title']
    list_filter = ['title']
    list_per_page = 10
    search_fields = ['title', 'leader__first_name', 'leader__last_name']  
    actions = [copy_groups,]  
    
    def view_on_site(self, obj):
        return reverse('groups_edit', kwargs={'sid':obj.id})


#models tuple
models = (Exam)
#register models
admin.site.register(models)
admin.site.register(Student, StudentAdmin)
admin.site.register(Groups, GroupAdmin)

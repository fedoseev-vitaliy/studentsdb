# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from ..models.student import Student
from ..my_paginator import MyPaginator, PageNotAnInteger, EmptyPage
from django.contrib import messages 
from django.views.generic import UpdateView, DeleteView
from students.forms import student_form
from django.views.generic.edit import CreateView
from django.views.decorators.csrf import ensure_csrf_cookie
import json

# Students Views
@ensure_csrf_cookie
def students_list(request):    
    students = Student.objects.all()
    
    if(request.POST and request.is_ajax()):
        std = Student.objects.get(pk=request.POST['checkbox_id'])
        std.delete_or_not = json.loads(request.POST['checkbox_value'])
        std.save()
    else:
        Student.objects.update(delete_or_not=False)
    
        #try to order students list
        order_by = request.GET.get('order_by', '')
        if order_by in ('first_name', 'last_name', 'ticket', 'pk'):
            students = students.order_by(order_by)
            if request.GET.get('reverse', '') == '1':
                students = students.reverse()
        
        #paginate students
        paginator = MyPaginator(students, 10)
        page = request.GET.get('page')
        try:
            students = paginator.page(page)
        except PageNotAnInteger:
            students = paginator.page(1)
        except EmptyPage:
            students = paginator.page(paginator.page_num)
            
        return render(request, 'students/students_list.html', {'students' : students})


def delete_multiple_students_view(request):
    template_name = 'forms/students_delete_form.html'
    students = Student.objects.filter(delete_or_not=True)
    
    if(request.POST):
        try:           
            students.delete()
            messages.success(request, u'Студенти були успішно видалені')  
                  
        except Exception:
            messages.error(request, u'Виникла помилка при видаленні студентів') 
        finally:
            return HttpResponseRedirect(reverse('home'))
    else:
        return render(request, template_name, {'students': students})


class StudentUpdateView(UpdateView):
    model = Student    
    template_name = 'forms/students_edit_form.html'
    form_class = student_form.StudentUpdateForm
    pk_url_kwarg = 'sid'       
    
    def get_success_url(self):
        messages.success(self.request, u'Студента успішно збережено!')
        return reverse('home')
    
    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button', None):
            messages.warning(request, u'Редагування студента відмінено!')
            return HttpResponseRedirect(reverse('home'))
        else:
            return UpdateView.post(self, request, *args, **kwargs)


class StudentsAddView(CreateView):
    model = Student    
    template_name = 'forms/students_add_form.html'
    form_class = student_form.StudentAddForm         
    
    
    def get_success_url(self):
        messages.success(self.request, u'Студента {} {} успішно додано!'.format(self.request.POST.get('first_name'), self.request.POST.get('last_name')))
        return reverse('home')
        
        
    def post(self, request, *args, **kwargs):
        if self.request.POST.get('cancel_button', None):
            messages.warning(self.request, u'Додавання студента скасовано!')
            return HttpResponseRedirect(reverse('home'))
        else:
            return CreateView.post(self, request, *args, **kwargs)


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'forms/student_delete_form.html'
    pk_url_kwarg = 'sid' 
    context_object_name = 'student'
    
    def get_success_url(self):
        messages.success(self.request, u'Студента успішно видалено!')
        return reverse('home')
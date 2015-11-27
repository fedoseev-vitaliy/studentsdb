# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from ..models.examination import Exam
from ..models.group import Groups
from ..forms import exam_form
from django.contrib import messages
from django.views.generic import CreateView
from ..my_paginator import MyPaginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

# Exams Views
def exam_list(request):
    exams = Exam.objects.all()
    
    #try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('exam_name', 'exam_date', 'teacher_name', 'pk'):
        exams = exams.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            exams = exams.reverse()
    
    #paginate students
    paginator = MyPaginator(exams, 10)
    page = request.GET.get('page')
    try:
        exams = paginator.page(page)
    except PageNotAnInteger:
        exams = paginator.page(1)
    except EmptyPage:
        exams = paginator.page(paginator.page_num)
        
    return render(request, 'students/exams_list.html', {'exams' : exams})


class ExamAddView(CreateView):
    model = Exam    
    template_name = 'forms/exam_add_form.html'
    form_class = exam_form.ExamAddForm      
    
    
    def get_success_url(self):
        messages.success(self.request, u'Іспит {} був успішно створений для групи {}'.format(
                                                                                        self.request.POST.get('exam_name'), 
                                                                                        Groups.objects.get(pk=self.request.POST.get('student_group')).title))
        return reverse('exams')
        
        
    def post(self, request, *args, **kwargs):
        if self.request.POST.get('cancel_button', None):
            messages.warning(self.request, u'Додавання іспиту скасовано!')
            return HttpResponseRedirect(reverse('exams'))
        else:
            return CreateView.post(self, request, *args, **kwargs)



def exam_group_result(request, sid):
    return HttpResponse('<h1>Group %s result</h1>' % sid)

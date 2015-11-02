from django.shortcuts import render
from django.http import HttpResponse
from ..models.examination import Exam
from ..my_paginator import MyPaginator, PageNotAnInteger, EmptyPage

# Exams Views
def exam_list(request):
    exams = Exam.objects.all()
    
    #try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('exam_name', 'exam_date', 'teacher_name', 'pk'):
        students = exams.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = exams.reverse()
    
    #paginate students
    paginator = MyPaginator(students, 10)
    page = request.GET.get('page')
    try:
        exams = paginator.page(page)
    except PageNotAnInteger:
        exams = paginator.page(1)
    except EmptyPage:
        exams = paginator.page(paginator.page_num)
        
    return render(request, 'students/exams_list.html', {'exams' : exams})


def exam_result(request):
    return HttpResponse('<h1>Exam result</h1>')

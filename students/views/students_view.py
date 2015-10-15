from django.shortcuts import render
from django.http import HttpResponse
from ..models import Student
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Students Views


def students_list(request):
    students = Student.objects.all()
    
    #try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('first_name', 'last_name', 'ticket', 'pk'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()
    
    #paginate students
    paginator = Paginator(students, 3)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        #if page not integer, render first page
        students = paginator.page(1)
    except EmptyPage:
        #if page out of range, return last page
        students = paginator.page(paginator.num_pages)
    
    return render(request, 'students/students_list.html', {'students':students})


def students_add(request):
    return HttpResponse('<h1>Student add form</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Student edit %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Student delete %s</h1>' % sid)
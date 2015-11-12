# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from ..models.student import Student
from ..models.group import Groups
from ..my_paginator import MyPaginator, PageNotAnInteger, EmptyPage
from datetime import datetime 
from PIL import Image
from django.contrib import messages 
from django.contrib.messages.api import get_messages
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
    paginator = MyPaginator(students, 10)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.page_num)
        
    return render(request, 'students/students_list.html', {'students' : students})


def students_add(request):
    # was form posted
    if (request.method == 'POST'):
        # was form add button clicked
        if (request.POST.get('add_button') is not None): 
                       
            # validate input data
            data = {'middle_name':request.POST.get('middle_name', ''),
                    'notes':request.POST.get('notes', ''),                    
                    }
            # get first name
            first_name=request.POST.get('first_name', '').strip()
            if (not first_name):
                messages.error(request, u'Ім\'я є обов\'язковим полем', extra_tags='first_name')                
            else:
                data['first_name'] = first_name
            
            # get last name
            last_name=request.POST.get('last_name', '').strip()
            if (not last_name):
                messages.error(request, u'Прізвище є обов\'язковим полем', extra_tags='last_name')                
            else:
                data['last_name'] = last_name
            
            #get birth day
            birth_day=request.POST.get('birth_day', '').strip()
            if (not birth_day):
                messages.error(request, u'Дата народження є обов\'язковим полем', extra_tags='birth_day')                 
            else:
                try:
                    datetime.strptime(birth_day, '%Y-%m-%d')
                except Exception:
                    messages.error(request, u'Дата народження має буду у форматі \'2015-10-31\'', extra_tags='birth_day')                     
                else:
                    data['birth_day'] = birth_day
            
            #get ticket
            ticket=request.POST.get('ticket', '').strip()
            if (not ticket):
                messages.error(request, u'Білет є обов\'язковим полем', extra_tags='ticket')                 
            else:
                data['ticket'] = ticket
            
            #get student group
            student_group=request.POST.get('student_group', '').strip()
            if (not student_group):
                messages.error(request, u'Група є обов\'язковим полем', extra_tags='student_group')                 
            else:
                group = Groups.objects.filter(pk=student_group)
                if (len(group) != 1):
                    messages.error(request, u'Оберіть існуючу групу', extra_tags='student_group')                       
                else:
                    data['student_group'] = group[0]
            
            #allowed_img = ('jpg', 'png')
            
            photo = request.FILES.get('photo', '')
            if (photo):
                try:
                    Image.open(photo.file, 'r').load()                    
                except IOError:
                    messages.error(request, u'Файл не є зображенням', extra_tags='photo')                    
                else:
                    data['photo'] = photo
            
            
            if (not get_messages(request)):
                # create Student object
                student = Student(**data)
                # save student to db
                student.save()
                
                messages.info(request, u'Студент {} {}  був успішно доданий!'.format(first_name, last_name))
                # redirect to home page
                return HttpResponseRedirect(reverse('home'))
                
            else:                           
                # render students_add html with errors
                return render(request, 'students/students_add.html', {'groups': Groups.objects.all().order_by('title'),})   
        elif(request.POST['cancel_button'] is not None):
            # redirect to home page on pressing cancel button
            messages.info(request, u'Додавання студента скасовано')
            return HttpResponseRedirect(reverse('home'))
    else:       
        # initial form renderer     
        return render(request, 'students/students_add.html', {'groups': Groups.objects.all().order_by('title')})


def students_edit(request, sid):
    return HttpResponse('<h1>Student edit %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Student delete %s</h1>' % sid)
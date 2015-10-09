from django.shortcuts import render
from django.http import HttpResponse


# Students Views


def students_list(request):
    students=(
        {'id':1,
         'first_name': u'Olena',
         'last_name': u'Fedosieieva',
         'ticket': 123,
         'image': 'img/olena.jpg'},
        {'id':2,
         'first_name': u'Yarik',
         'last_name': u'Kovalchuk',
         'ticket': 124,
         'image': 'img/yarik.jpg'},
        {'id':3,
         'first_name': u'Vitalii',
         'last_name': u'Fedosieiev',
         'ticket': 125,
         'image': 'img/me.jpg'},)
    
    return render(request, 'students/students_list.html', {'students':students})


def students_add(request):
    return HttpResponse('<h1>Student add form</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Student edit %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Student delete %s</h1>' % sid)
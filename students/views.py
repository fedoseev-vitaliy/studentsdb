from django.shortcuts import render
from django.http import HttpResponse


# Students Views


def students_list(request):
    return render(request, 'students/students_list.html', {})


def students_add(request):
    return HttpResponse('<h1>Student add form</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Student edit %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Student delete %s</h1>' % sid)


# Group Views


def groups_list(request):
    return HttpResponse('<h1>Group Listing</h1>')


def groups_add(request):
    return HttpResponse('<h1>Group add form</h1>')


def groups_edit(request, sid):
    return HttpResponse('<h1>Group edit %s</h1>' % sid)


def groups_delete(request, sid):
    return HttpResponse('<h1>Group delete %s</h1>' % sid)
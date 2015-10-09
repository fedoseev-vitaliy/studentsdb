from django.shortcuts import render
from django.http import HttpResponse

def journals_list(request):
    students=(
        {'id':1,
         'first_name': u'Olena',
         'last_name': u'Fedosieieva',},
        {'id':2,
         'first_name': u'Yarik',
         'last_name': u'Kovalchuk',},
        {'id':3,
         'first_name': u'Vitalii',
         'last_name': u'Fedosieiev',},)
    
    return render(request, 'students/journals_list.html', {'students':students})


def journal_student_view(request, sid):
    return HttpResponse('<h1>Student journal %s</h1>' % sid)


def journal_group_view(request, sid):
    return HttpResponse('<h1>Group journal %s</h1>' % sid)

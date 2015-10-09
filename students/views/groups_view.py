from django.shortcuts import render
from django.http import HttpResponse


# Group Views


def groups_list(request):
    groups = (
        {'id': 1,
         'name': u'MtM',
         'starosta': u'Olena Fedosieieva'},
        {'id': 2,
         'name': u'MtM2',
         'starosta': u'Vitalii Fedosieiev'},)    
    return render(request, 'students/groups_list.html', {'groups': groups})


def groups_add(request):
    return HttpResponse('<h1>Group add form</h1>')


def groups_edit(request, sid):
    return HttpResponse('<h1>Group edit %s</h1>' % sid)


def groups_delete(request, sid):
    return HttpResponse('<h1>Group delete %s</h1>' % sid)
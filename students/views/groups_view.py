from django.shortcuts import render
from django.http import HttpResponse
from ..models import Groups
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Group Views


def groups_list(request):
    groups = Groups.objects.all()
    
    #try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('pk', 'title', 'leader'):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            groups = groups.reverse()
    
    #paginate students
    paginator = Paginator(groups, 10)
    page = request.GET.get('page')
    try:
        groups = paginator.page(page)
    except PageNotAnInteger:
        groups = paginator.page(1)
    except EmptyPage:
        groups = paginator.page(paginator.page_num)
        
    return render(request, 'students/groups_list.html', {'groups': groups})


def groups_add(request):
    return HttpResponse('<h1>Group add form</h1>')


def groups_edit(request, sid):
    return HttpResponse('<h1>Group edit %s</h1>' % sid)


def groups_delete(request, sid):
    return HttpResponse('<h1>Group delete %s</h1>' % sid)
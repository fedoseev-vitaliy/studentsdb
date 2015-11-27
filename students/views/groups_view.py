# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from ..models.group import Groups
from ..models.student import Student
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, DeleteView, UpdateView
from students.forms import group_form
from django.views.decorators.csrf import ensure_csrf_cookie
import json
from django.contrib.messages.api import get_messages

# Group Views
@ensure_csrf_cookie
def groups_list(request):    
    groups = Groups.objects.all()
        
    if(request.POST and request.is_ajax()):
        group = Groups.objects.get(pk=request.POST['checkbox_id'])
        group.delete_or_not = json.loads(request.POST['checkbox_value'])
        group.save()
    else:
        Groups.objects.update(delete_or_not=False)
        
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


def delete_multiple_groups(request):
    template_name = 'forms/groups_delete_form.html' 
    groups = Groups.objects.filter(delete_or_not=True)
        
    if(request.POST):
        try:           
            groups.delete()
            messages.success(request, u'Група була успішно видалена')  
                  
        except Exception:
            messages.error(request, u'Виникла помилка при видаленні групи') 
        finally:
            return HttpResponseRedirect(reverse('groups'))
    else:
        return render(request, template_name, {'groups': groups})
    
    
class AddGroupView(CreateView):
    model = Groups
    template_name = 'forms/groups_add_form.html'
    form_class = group_form.GroupAddForm
    
    def get_success_url(self):
        messages.success(self.request, u'Група {} успішно додана!'.format(self.request.POST.get('title')))
        return reverse('groups')
        
        
    def post(self, request, *args, **kwargs):
        if self.request.POST.get('cancel_button', None):
            messages.warning(self.request, u'Додавання групи скасовано!')
            return HttpResponseRedirect(reverse('groups'))
        else:
            return CreateView.post(self, request, *args, **kwargs)
        
# def add_group_view(request):
#     if(request.POST):
#         if(request.POST.get('add_button')):
#             data = {'notes': request.POST.get('notes', '')}
#             
#             title = request.POST.get('title', '')
#             if not title:
#                 messages.error(request, u'Це поле є обов\'язковим')
#             else:
#                 data['title'] = title
#                 
#             leader = request.POST.get('leader', '')
#             if not leader:
#                 messages.error(request, u'Це поле є обов\'язковим')
#             else:
#                 groups = Groups.objects.filter(leader=leader)
#                 if(len(groups) > 0):
#                     messages.error(request, u'Цей студент вже є староста іншої групи')
#                 else:
#                     data['leader']= leader
#             
#             if(not get_messages()):
#                 new_group = Groups(**data)
#                 new_group.save()
#                 messages.success(request, u'Група {} була додана успішно'.format(title))
#             return HttpResponseRedirect(reverse('groups_add'))
#         else:            
#             return HttpResponseRedirect(reverse('groups_add'))        
#     else:
#         #group_students = Student.objects.filter(student_group=request.GET.get('title', ''))        
#         return render(request, 'forms/groups_add_form_function.html', {})
    

class DeleteGroupView(DeleteView):
    model = Groups
    template_name = 'forms/group_delete_form.html'
    pk_url_kwarg = 'sid' 
    context_object_name = 'group'
    
    def get_success_url(self):
        messages.success(self.request, u'Група успішно видалена!')
        return reverse('groups')
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            self.object.delete()  
            return HttpResponseRedirect(self.get_success_url())          
        except Exception:
            messages.error(self.request, u'Виникла помилка при видаленні групи')
            return HttpResponseRedirect(reverse('groups'))
        
        
class EditGroupView(UpdateView):
    model = Groups    
    template_name = 'forms/groups_edit_form.html'
    form_class = group_form.GroupUpdateForm
    pk_url_kwarg = 'sid'       
    
    def get_success_url(self):
        messages.success(self.request, u'Група успішно збережена!')
        return reverse('groups')
    
    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button', None):
            messages.warning(request, u'Редагування групи відмінено!')
            return HttpResponseRedirect(reverse('groups'))
        else:
            return UpdateView.post(self, request, *args, **kwargs)
        
    
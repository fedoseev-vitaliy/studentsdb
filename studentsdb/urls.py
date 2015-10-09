from django.conf.urls import include, url
from django.contrib import admin
from students.views import students_view, groups_view, journals_view


urlpatterns = [
               
               
    #Students url
    url(r'^$', students_view.students_list, name='home'),
    url(r'^students/add/$', students_view.students_add, name='students_add'),
    url(r'^students/(?P<sid>\d+)/edit/$', students_view.students_edit, name='students_edit'),
    url(r'^students/(?P<sid>\d+)/delete/$', students_view.students_delete, name='students_delete'),
    
    
    #Group url    
    url(r'^groups/$', groups_view.groups_list, name='groups'),  
    url(r'^groups/add/$', groups_view.groups_add, name='groups_add'),
    url(r'^groups/(?P<sid>\d+)/edit/$', groups_view.groups_edit, name='groups_edit'),
    url(r'^groups/(?P<sid>\d+)/delete/$', groups_view.groups_delete, name='groups_delete'),
    
    
    # Journal url
    url(r'^journal/$', journals_view.journals_list, name="journals"),
    url(r'^journal/student/(?P<sid>\d+)/view/$', journals_view.journal_student_view, name="journal_student_view"),
    url(r'^journal/group/(?P<sid>\d+)/view/$', journals_view.journal_group_view, name="journal_group_view"),
    
    
    #Admin urls             
    url(r'^admin/', include(admin.site.urls)),
]

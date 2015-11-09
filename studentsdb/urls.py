from django.conf.urls import include, url
from django.contrib import admin
from students.views import students_view, groups_view, journals_view,\
    examination_view
from settings import DEBUG, MEDIA_ROOT


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
    
    
    # Exam url
    url(r'^exam/$', examination_view.exam_list, name="exams"),    
    url(r'^exam/group/(?P<sid>\d+)/view/$', examination_view.exam_group_result, name="group_result"),
    
    
    
    #Admin urls             
    url(r'^admin/', include(admin.site.urls)),
]




if DEBUG:
    #serve files from media root
    urlpatterns += [
    
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
]
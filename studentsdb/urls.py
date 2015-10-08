from django.conf.urls import include, url
from django.contrib import admin
from students import views 


urlpatterns = [
               
               
    #Students url
    url(r'^$', views.students_list, name='home'),
    url(r'^students/add/$', views.students_add, name='students_add'),
    url(r'^students/(?P<sid>\d+)/edit/$', views.students_edit, name='students_edit'),
    url(r'^students/(?P<sid>\d+)/delete/$', views.students_delete, name='students_delete'),
    
    
    #Group url    
    url(r'^groups/$', views.groups_list, name='groups'),  
    url(r'^groups/add/$', views.groups_add, name='groups_add'),
    url(r'^groups/(?P<sid>\d+)/edit/$', views.students_edit, name='groups_edit'),
    url(r'^groups/(?P<sid>\d+)/delete/$', views.students_delete, name='groups_delete'),
    
    
    #Admin urls             
    url(r'^admin/', include(admin.site.urls)),
]

# -*- coding: utf-8 -*-

from django.db import models
from student import Student


class Groups(models.Model):
    """ Groups model """
    
    class Meta(object):
        verbose_name = u'Група'
        verbose_name_plural = u'Групи'
       
    title = models.CharField(max_length=256, blank=False, verbose_name=u'Групи')
    leader = models.OneToOneField(Student, verbose_name = u'Староста', blank=True, null=True, on_delete=models.SET_NULL)    
    notes = models.TextField(blank=True, verbose_name=u'Нотатки')
        
    def __unicode__(self):
        return u'%s' % (self.title)            
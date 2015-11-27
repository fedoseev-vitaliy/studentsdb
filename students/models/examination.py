# -*- coding: utf-8 -*-
from django.db import models

class Exam(models.Model):
    """ Exam model """
    
    class Meta(object):
        verbose_name = u'Іспит'
        verbose_name_plural = u'Іспити'
       
    exam_name = models.CharField(max_length=256, blank=False, verbose_name=u'Назва іспиту')
    exam_date = models.DateField(blank=False, verbose_name=u'Дата іспиту', null=True)
    teacher_name = models.CharField(max_length=256, blank=False, verbose_name=u'Викладач')    
    student_group = models.ForeignKey('Groups', verbose_name=u'Група', blank=False, null=True, on_delete=models.PROTECT)
        
    def __unicode__(self):
            return u'%s' % (self.exam_name)

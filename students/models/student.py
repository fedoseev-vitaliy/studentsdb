# -*- coding: utf-8 -*-

from django.db import models

class Student(models.Model):
    """ Student model """
    
    class Meta(object):
        verbose_name = u'Студент'
        verbose_name_plural = u'Студенти'
       
    first_name = models.CharField(max_length=256, blank=False, verbose_name=u'Імя')
    last_name = models.CharField(max_length=256, blank=False, verbose_name=u'Призвище')
    middle_name = models.CharField(max_length=256, blank=True, verbose_name=u'По-батькові', default='')
    birth_day = models.DateField(blank=False, verbose_name=u'Дата народження', null=True)
    photo = models.ImageField(blank=True, verbose_name=u'Фото', null=True)
    ticket = models.CharField(max_length=256, blank=False, verbose_name=u'Білет')
    notes = models.TextField(blank=True, verbose_name=u'Нотатки')
    student_group = models.ForeignKey('Groups', verbose_name=u'Група', blank=False, null=True, on_delete=models.PROTECT)
        
    def __unicode__(self):
            return u"%s %s" % (self.first_name, self.last_name)
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django import forms
from django.core.mail import send_mail
from studentsdb.settings import ADMIN_EMAIL
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def contact_admin(request):
    #check if form was posted
    if request.method == 'POST':
        #create a form instance an populate with data
        form = ContactForm(request.POST)
        
        #check if input data is correct
        if form.is_valid():
            #send email
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']
            
            try:
                send_mail(subject, message, from_email, [ADMIN_EMAIL])
            except Exception:
                message = u'Під час відправки листа виникла непередбачувальна помилка. \
                           Спробуйте скористатися формою пізніше.'
            else:
                message = u'Повідомлення успішно надіслане'
            
            messages.info(request, message)
            # redirect to same page with success message
            return HttpResponseRedirect(reverse('contact_admin'))
        
    else:
        form = ContactForm()
            
    return render(request, 'contact_admin/form.html', {'form':form})


class ContactForm(forms.Form):
    from_email = forms.EmailField(label=u'Ваша Емейл Адреса')    
    subject = forms.CharField(label=u'Заголовок листа', max_length=128)
    message = forms.CharField(label=u'Текст повідомлення', max_length=2560, widget=forms.Textarea)
    
    
    
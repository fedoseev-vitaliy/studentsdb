# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.mail import send_mail
from studentsdb.settings import ADMIN_EMAIL
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

def contact_admin(request):
    #check if form was posted
    if request.method == 'POST':
        #create a form instance an populate with data
        form = ContactAdminForm(request.POST)        
        #check if input data is correct
        if form.is_valid():   
            # send email
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']       
            try:
                send_mail(subject, message, from_email, [ADMIN_EMAIL])                             
            except Exception:
                message = u'Під час відправки листа виникла непередбачувальна помилка. \
                           Спробуйте скористатися формою пізніше.'
                messages.error(request, message)
            else:
                message = u'Повідомлення успішно надіслане'            
                messages.success(request, message)
            return HttpResponseRedirect(reverse('contact_admin'))
                 
    else:
        form = ContactAdminForm()        
    return render(request, 'contact_admin/form.html', {'form':form})

 
class ContactAdminForm(forms.Form):
    def __init__(self, *args, **kwargs):
        #call origin initializator
        super(ContactAdminForm, self).__init__(*args, **kwargs)
          
        #init FormHelper 
        self.helper = FormHelper()
          
        #form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'        
          
        #twitter bootstrap style
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-lable'
        self.helper.field_class = 'col-sm-10'
          
        #form submit button
        self.helper.add_input(Submit('send_button', u'Надіслати'))        
    
    from_email = forms.EmailField(label=u"Ваша Емейл Адреса")
    subject = forms.CharField(label=u"Заголовок листа", max_length=128)
    message = forms.CharField(label=u"Текст повідомлення", widget=forms.Textarea)
    
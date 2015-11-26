# -*- coding: utf-8 -*-
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.core.mail import send_mail
from studentsdb.settings import ADMIN_EMAIL


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
    
    from_email = forms.EmailField(label=u"електронна адреса")
    subject = forms.CharField(label=u"заголовок", max_length=128)
    message = forms.CharField(label=u"текст повідомлення", widget=forms.Textarea)
    
    #method to send email to adimn team
    def send_email(self):
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']
        from_email = self.cleaned_data['from_email']
        
        send_mail(subject, message, from_email, [ADMIN_EMAIL])
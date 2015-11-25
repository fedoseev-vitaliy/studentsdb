# -*- coding: utf-8 -*-
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions
from django.core.urlresolvers import reverse
from ..models.student import Student

student_fields = ['first_name', 'middle_name', 'last_name', 'birth_day', 'photo', 'ticket', 'notes'] 

class StudentUpdateForm(ModelForm):
    class Meta:
        model = Student       
        fields = student_fields
        
    def __init__(self, *args, **kwargs):
        #call origin initializator
        super(StudentUpdateForm, self).__init__(*args, **kwargs)
          
        #init FormHelper 
        self.helper = FormHelper(self)
        # set form tag attributes
        self.helper.form_action = reverse('students_edit', kwargs={'sid': kwargs['instance'].id})  
        #form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'        
          
        #twitter bootstrap style
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-lable'
        self.helper.field_class = 'col-sm-10'
          
        #form submit button             
        self.helper.layout.append(FormActions(
                                    Submit('add_button', u'Зберегти', css_class="btn btn-primary"),
                                    Submit('cancel_button', u'Скасувати', css_class="btn btn-link"),
                                    )) 
        
class StudentAddForm(ModelForm):
    class Meta:
        model = Student       
        fields = student_fields
        
    def __init__(self, *args, **kwargs):
        #call origin initializator
        super(StudentAddForm, self).__init__(*args, **kwargs)
                  
        #init FormHelper 
        self.helper = FormHelper(self)        
        
        #form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'        
        self.helper.form_action = reverse('students_add')  
        #twitter bootstrap style
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-lable'
        self.helper.field_class = 'col-sm-10'
          
        #form submit button             
        self.helper.layout.append(FormActions(
                                    Submit('add_button', u'Додати', css_class="btn btn-primary"),
                                    Submit('cancel_button', u'Скасувати', css_class="btn btn-link"),
                                    ))    
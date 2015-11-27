# -*- coding: utf-8 -*-
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions
from django.core.urlresolvers import reverse
from ..models.examination import Exam
from django.forms.widgets import DateInput, Select
    
class ExamAddForm(ModelForm):
    class Meta:
        model = Exam       
        fields = '__all__'
        widgets = {
            'exam_date': DateInput(attrs={'id': 'datepicker'}),
            'student_group': Select,
            }
        
    def __init__(self, *args, **kwargs):
        #call origin initializator
        super(ExamAddForm, self).__init__(*args, **kwargs)
          
        #init FormHelper 
        self.helper = FormHelper(self)
        # set form tag attributes
        self.helper.form_action = reverse('exam_add')  
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
                                    css_class="col-sm-offset-2 col-sm-10",
                                    ))        
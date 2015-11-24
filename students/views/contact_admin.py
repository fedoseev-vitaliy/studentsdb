# -*- coding: utf-8 -*-
from django.contrib import messages
from django.views.generic.edit import FormView
from ..forms import contact_admin_form

class ContacAdminView(FormView):
    template_name = 'forms/form.html'
    form_class = contact_admin_form.ContactAdminForm
    success_url = '/contact/'
    
    def form_valid(self, form):
        try:
            form.send_email()
            message = u'Повідомлення успішно надіслане'            
            messages.success(self.request, message)
        except Exception:
            message = u'Під час відправки листа виникла непередбачувальна помилка. \
                        Спробуйте скористатися формою пізніше.'
            messages.error(self.request, message)
        return FormView.form_valid(self, form)
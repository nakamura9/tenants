from django.shortcuts import render
from tenant_app import forms
import os
from django.views.generic import FormView, TemplateView
from django.views.generic.edit import FormMixin
from tenant_app.utils import get_tenant_from_request
# Create your views here.

class TenantInitialMixin(FormMixin):
    def get_initial(self):
        initial = super().get_initial()
        initial['tenant'] = get_tenant_from_request(self.request)
        initial['creator'] = self.request.user
        return initial
    
class TenantListMixin(object):
    def get_queryset(self):
        tenant = get_tenant_from_request(self.request)
        return super().get_queryset().filter(tenant=tenant)
        

class HomeView(TemplateView):
    template_name = os.path.join('tenant_app', 'home.html')

class LoginView(FormView):
    form_class = forms.LoginForm
    template_name = os.path.join('tenant_app', 'login.html')
    success_url = "/home/"

    def form_valid(self, form):
        resp = super().form_valid(form)
        self.request.session['tenant_id'] = form.cleaned_data['company_id']
        return resp
    
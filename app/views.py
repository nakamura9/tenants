from django.shortcuts import render
from django.views.generic import CreateView, ListView
import os 
from app.forms import CustomerForm, ItemForm
from app.models import Customer, Item
from tenant_app.views import TenantInitialMixin, TenantListMixin
# Create your views here.

class CustomerCreateView(TenantInitialMixin, CreateView):
    model_name = Customer
    form_class = CustomerForm
    success_url = '/customer-list/'
    template_name = os.path.join('app', 'customer_create.html')
    
class ItemCreateView(TenantInitialMixin, CreateView):
    model_name = Item
    form_class = ItemForm
    success_url = '/item-list/'
    template_name = os.path.join('app', 'item_create.html')
    
    
class ItemListView(TenantListMixin, ListView):
    model = Item
    template_name = os.path.join('app', 'item_list.html')
    
class CustomerListView(TenantListMixin, ListView):
    model = Customer
    template_name = os.path.join('app', 'customer_list.html')
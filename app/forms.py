from django import forms 
from app.models import Customer, Item

class ItemForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = Item
        
        
class CustomerForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = Customer
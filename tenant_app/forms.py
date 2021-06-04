from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    company_id = forms.CharField(widget=forms.NumberInput)
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        if not authenticate(username=cleaned_data['username'], 
                            password=cleaned_data['password']):
            raise forms.ValidationError("Username or Password incorrect.")
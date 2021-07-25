from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import Phone, Email, Account

class PhoneForm(forms.ModelForm):
    
    class Meta:
        model = Phone
        fields = "__all__"
        labels = {
            "phone": "Phone"
        }
        # widgets = {
        #     'phone': forms.TextInput(attrs={'class': 'form-control'}),
        # }


class EmailForm(forms.ModelForm):

    class Meta:
        model = Email
        fields = "__all__"
        labels = {
            "email": "Email"
        }


class AccountForm(forms.ModelForm):

    class Meta:
        model = Account
        exclude = ['login_code']
        labels = {
            "category": "Category",
            "username": "Username",
            "password": "Password",
            "email_id": "Email Address",
            "phone_id": "Phone Number",
            # "login_code": "Recovery Codes",
        }
        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'email_id': forms.Select(attrs={'class': 'form-control'}),
            'phone_id': forms.Select(attrs={'class': 'form-control'}),
            'login_code': forms.TextInput(attrs={'class': 'form-control'}),
        }

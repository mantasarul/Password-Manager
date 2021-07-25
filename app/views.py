from django.views.generic.detail import DetailView
from app.forms import AccountForm, EmailForm, PhoneForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.views.generic.list import ListView

from .models import Email, Phone, Account, Codes

# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"


class AddPhoneView(CreateView, ListView):
    model = Phone
    form_class = PhoneForm
    template_name = "add-phone.html"
    success_url = 'add-phone'


class AddEmailView(CreateView, ListView):
    model = Email
    form_class = EmailForm
    template_name = 'add-email.html'
    success_url = 'add-email'


class AddAccountView(CreateView):
    model = Account
    form_class = AccountForm
    template_name = 'add-account.html'
    success_url = 'home'


class AllAccountView(ListView):
    template_name = 'all-account.html'
    model = Account


class TestView(TemplateView):
    template_name = 'test.html'


class LoginCodeView(ListView):
    template_name = 'all-code.html'
    model = Codes


class EditPhoneView(UpdateView):
    model = Phone
    template_name = 'add-phone.html'
    fields = '__all__'
    success_url = '/add-phone'


class EditEmailView(UpdateView):
    model = Email
    template_name = 'add-email.html'
    fields = '__all__'
    success_url = '/add-email'

class EditAccountView(UpdateView):
    model = Account
    template_name = 'add-account.html'
    fields = '__all__'
    success_url = '/all-account'


class DeletePhoneView(DeleteView):
    model = Phone
    template_name = 'delete-phone.html'
    success_url = '/add-phone'


class DeleteEmailView(DeleteView):
    model = Email
    template_name = 'delete-email.html'
    success_url = '/add-email'


class DeleteAccountView(DeleteView):
    model = Account
    template_name = 'delete-account.html'
    success_url = '/all-account'


class DeleteLoginView(DeleteView):
    pass




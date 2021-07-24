from django.contrib import admin
from .models import Email, Phone, Account, Codes

# Register your models here.

class EmailModel(admin.ModelAdmin):
    list_display = ['email']


class PhoneModel(admin.ModelAdmin):
    list_display = ['phone']


class AccountModel(admin.ModelAdmin):
    list_display = ['category', 'username', 'password', 'email_id', 'phone_id', 'login_code']


class CodesModel(admin.ModelAdmin):
    list_display = ['code']


admin.site.register(Email, EmailModel)
admin.site.register(Phone, PhoneModel)
admin.site.register(Account, AccountModel)
admin.site.register(Codes, CodesModel)
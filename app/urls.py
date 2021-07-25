from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('add-phone', views.AddPhoneView.as_view(), name='add-phone'),
    path('add-email', views.AddEmailView.as_view(), name='add-email'),
    path('add-account', views.AddAccountView.as_view(), name='add-account'),
    path('all-account', views.AllAccountView.as_view(), name='all-account'),
    path('test', views.TestView.as_view(), name='test'),
    path('all-code', views.LoginCodeView.as_view(), name='all-code'),
    path('edit-phone/<pk>', views.EditPhoneView.as_view(), name='edit-phone'),
    path('edit-email/<pk>', views.EditEmailView.as_view(), name='edit-email'),
    path('edit-account/<pk>', views.EditAccountView.as_view(), name='edit-account'),
    path('delete-phone/<pk>', views.DeletePhoneView.as_view(), name='delete-phone'),
    path('delete-email/<pk>', views.DeleteEmailView.as_view(), name='delete-email'),
    path('delete-account/<pk>', views.DeleteAccountView.as_view(), name='delete-account'),
]

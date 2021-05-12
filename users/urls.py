from django.contrib import admin
from django.urls import path, include
from .views import user_account, contact_us, account_login

urlpatterns = [
    path('user_account/', user_account,
         name='user_account'),
    path('contact_us/', contact_us,
         name='contact_us'),
    path('account_login/', account_login,
         name='account_login')
]

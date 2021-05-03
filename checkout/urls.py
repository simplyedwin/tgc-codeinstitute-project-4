from django.contrib import admin
from django.urls import path, include
import checkout.views

urlpatterns = [
    path('',
         checkout.views.checkout, name="checkout"),
    path('checkout_completed/',
         checkout.views.checkout_completed, name="checkout_completed"),
    path('checkout_not_completed/',
         checkout.views.checkout_not_completed, name="checkout_not_completed"),

]

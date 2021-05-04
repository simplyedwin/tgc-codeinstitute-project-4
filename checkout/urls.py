from django.contrib import admin
from django.urls import path, include
from .views import checkout, payment_completed, order_completed, order_not_completed

urlpatterns = [
    path('', checkout, name="checkout"),
    path('order_completed/',
         order_completed, name="order_completed"),
    path('order_not_completed/',
         order_not_completed, name="order_not_completed"),
    path('payment_completed', payment_completed)

]

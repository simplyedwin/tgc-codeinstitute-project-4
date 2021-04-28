from django.contrib import admin
from django.urls import path, include
import users.views

urlpatterns = [
    path('products/shop', users.views.shop_page,
         name='shop_page'),
]

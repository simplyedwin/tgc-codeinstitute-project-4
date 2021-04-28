from django.contrib import admin
from django.urls import path, include
import products.views

urlpatterns = [
    path('products/', products.views.shop_page,
         name='shop_page'),
]

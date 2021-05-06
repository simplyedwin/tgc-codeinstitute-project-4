from django.contrib import admin
from django.urls import path, include
from .views import shop_page, product_page
urlpatterns = [
    path('shop/', shop_page,
         name='shop_page'),
    path('product/<plant_id>', product_page,
         name='product_page')
]

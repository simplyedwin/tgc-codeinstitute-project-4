from django.contrib import admin
from django.urls import path, include
from .views import shop_page, product_page, about_us
urlpatterns = [
    path('shop/', shop_page,
         name='shop_page'),
    path('about_us/', about_us,
         name='about_us'),
    path('product/<plant_id>', product_page,
         name='product_page')

]

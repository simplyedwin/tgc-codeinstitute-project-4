from django.contrib import admin
from django.urls import path, include
from .views import create_review

urlpatterns = [
    path('<order_id>', create_review,
         name='create_review'),
]

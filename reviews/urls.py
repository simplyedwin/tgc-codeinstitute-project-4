from django.contrib import admin
from django.urls import path, include
from .views import write_review, create_review

urlpatterns = [
    path('write_review/<order_id>', write_review,
         name='write_review'),
    path('create_review/<order_id>', create_review,
         name='create_review')

]

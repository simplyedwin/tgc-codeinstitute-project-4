from django.shortcuts import render, reverse, redirect, get_object_or_404

# Create your views here.


def index(request):

    return render(request, 'landing_page-template.html')


def shop_page(request):

    return render(request, 'products/shop_page-template.html')

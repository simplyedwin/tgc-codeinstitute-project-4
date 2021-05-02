from django.shortcuts import render, reverse, redirect, get_object_or_404
from products.models import Plant

# Create your views here.


def index(request):

    return render(request, 'products/landing_page-template.html')


def shop_page(request):

    plants = Plant.objects.all()

    cart = request.session['shopping_cart']

    return render(request, 'products/shop_page-template.html',
                  {'plants': plants, 'cart': cart})

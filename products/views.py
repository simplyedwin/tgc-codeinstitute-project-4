from django.shortcuts import render, reverse, redirect, get_object_or_404
from products.models import Plant
from reviews.models import Review
from django.db.models import Q


# Create your views here.


def index(request):

    return render(request, 'products/landing_page-template.html')


def shop_page(request):

    plants = Plant.objects.all()

    cart = request.session.get('shopping_cart', {})

    return render(request, 'products/shop_page-template.html',
                  {'plants': plants, 'cart': cart})


def product_page(request, plant_id):

    # to retrieve the plant to display on product page
    plant = get_object_or_404(Plant, pk=plant_id)
    # to filter by plant type
    query = Q(plant__exact=plant)
    # to retrieve all reviews
    reviews = Review.objects.all()
    # to retrieve all the reviews for the plant
    plant_reviews = reviews.filter(query).values().distinct()

    return render(request, "products/product_page-template.html",
                  {"plant": plant, "plant_reviews": plant_reviews})

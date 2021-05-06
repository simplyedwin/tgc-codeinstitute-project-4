from django.shortcuts import render, reverse, redirect, get_object_or_404
from products.models import Plant
from reviews.models import Review
from django.db.models import Q
from django.contrib.auth.models import User
from django.db.models.aggregates import Avg


# Create your views here.


def index(request):

    return render(request, 'products/landing_page-template.html')


def shop_page(request):

    plants = Plant.objects.all()

    # to determine the qty of items in cart
    cart = request.session.get('shopping_cart', {})

    return render(request, 'products/shop_page-template.html',
                  {'plants': plants, 'cart': cart})


def product_page(request, plant_id):

    # to retrieve all users
    users = User.objects.all()
    # to retrieve the plant to display on product page
    plant = get_object_or_404(Plant, pk=plant_id)
    # to filter by plant type
    query = Q(plant__exact=plant)
    # to retrieve all reviews
    reviews = Review.objects.all()
    # to retrieve all the reviews for the plant
    plant_reviews = reviews.filter(query).values().distinct()

    # to retrieve ave ratings of the selected plant
    plant_ave_rating = plant_reviews.aggregate(Avg('rating'))

    # to retrieve total number of reviews for the selected plant
    plant_total_reviews = plant_reviews.count()

    if plant_ave_rating != None and plant_total_reviews:

        plant.rating = float(plant_ave_rating['rating__avg'])

        plant.save(update_fields=["rating"])

        plant.reviews = plant_total_reviews

        plant.save(update_fields=["reviews"])

    return render(request, "products/product_page-template.html",
                  {"plant": plant, "users": users,
                   "plant_reviews": plant_reviews})

from django.shortcuts import render, reverse, redirect, get_object_or_404
from products.models import Plant
from reviews.models import Review
from django.db.models import Q
from django.contrib.auth.models import User
from django.db.models.aggregates import Avg


# Create your views here.

# this view shows the landing page
def index(request):

    # to determine the qty of items in cart
    cart = request.session.get('shopping_cart', {})

    return render(request, 'products/landing_page-template.html',
                  {'cart': cart})

# this view display the information about the e-shop


def about_us(request):

    # to determine the qty of items in cart
    cart = request.session.get('shopping_cart', {})

    return render(request, 'products/about_us-template.html', {'cart': cart})

# this view show the overview product page


def shop_page(request):

    # to retrieve all the plants
    plants = Plant.objects.all()
    # to retrieve the query in the search box
    search_query = request.GET
    # run the search engine if there is query provided
    if search_query:

        query = Q(name__icontains=search_query['search-input']) | Q(
            species__icontains=search_query['search-input']) | Q(
            size__icontains=search_query['search-input']) | Q(
            description__icontains=search_query['search-input']) | Q(
            reviews__icontains=search_query['search-input']) | Q(
            watering__icontains=search_query['search-input']) | Q(
            sunlight__icontains=search_query['search-input']) | Q(
            level__icontains=search_query['search-input']) | Q(
            country__icontains=search_query['search-input'])

        plants = plants.filter(query)

        # display no result found page if no result is found
        if not plants:

            return render(request, 'products/no_result-template.html')

    # to determine the qty of items in cart
    cart = request.session.get('shopping_cart', {})

    return render(request, 'products/shop_page-template.html',
                  {'plants': plants, 'cart': cart})

# this view show the product page


def product_page(request, plant_id):

    # to determine the qty of items in cart
    cart = request.session.get('shopping_cart', {})

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

    # to save the plant total reviews and average ratings
    if plant_ave_rating != None and plant_total_reviews:

        plant.rating = float(plant_ave_rating['rating__avg'])

        plant.save(update_fields=["rating"])

        plant.reviews = plant_total_reviews

        plant.save(update_fields=["reviews"])

    return render(request, "products/product_page-template.html",
                  {"plant": plant, "users": users,
                   "plant_reviews": plant_reviews, 'cart': cart})

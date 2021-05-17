from django.shortcuts import get_object_or_404, redirect, render, reverse
from reviews.forms import ReviewForm
from checkout.models import Order
from django.contrib import messages
from users.views import user_account
from products.models import Plant
from django.db.models import Avg, Q
from reviews.models import Review


# Create your views here.

# this view shows the review form
def write_review(request, order_id):

    order_model = get_object_or_404(Order, pk=order_id)

    review_form = ReviewForm(request.POST or None)

    return render(request, "reviews/user_review-template.html",
                  {"form": review_form, "order": order_model})

# this view save the user review into the database


def create_review(request, order_id):

    order_model = get_object_or_404(Order, pk=order_id)

    if request.method == "POST":

        review_form = ReviewForm(request.POST)

        # save the review into the database and flash out a review
        # successfully added message
        if review_form.is_valid():

            filled_review_form = review_form.save(commit=False)

            filled_review_form.reviewed_by = request.user

            filled_review_form.plant = order_model.plant

            filled_review_form.order = order_model

            filled_review_form.save()

            # to retrieve the plant to display on product page
            plant = get_object_or_404(Plant, pk=filled_review_form.plant.id)

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

            messages.success(request, "Your review is successfully added.")

            return redirect(reverse(user_account))

        else:

            create_review_form = ReviewForm()

            return render(request, 'reviews/user_review-template.html', {
                'form': create_review_form,
                "order": order_model
            })

    else:

        create_review_form = ReviewForm()

        return render(request, 'reviews/user_review-template.html', {
            'form': create_review_form,
            "order": order_model
        })

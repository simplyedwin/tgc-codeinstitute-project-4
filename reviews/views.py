from django.shortcuts import get_object_or_404, redirect, render, reverse
from reviews.forms import ReviewForm
from checkout.models import Order
from django.contrib import messages
from users.views import user_account


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

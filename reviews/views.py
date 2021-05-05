from django.shortcuts import get_object_or_404, render
from reviews.forms import ReviewForm
from checkout.models import Order

# Create your views here.


def create_review(request, order_id):

    order_model = get_object_or_404(Order, pk=order_id)

    review_form = ReviewForm(request.POST or None)

    return render(request, "reviews/user_review-template.html",
                  {"form": review_form, "order": order_model})

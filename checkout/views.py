from django.shortcuts import render, reverse, HttpResponse, get_object_or_404
from django.conf import settings
import stripe
from products.models import Plant
import json

# Create your views here.


def checkout(request):

    stripe.api_key = settings.STRIPE_SECRET_KEY

    # To pass shopping cart to STRIPE
    cart = request.session.get('shopping_cart', {})

    # To create line items in the cart
    cart_items = []

    #
    all_plant_ids = []

    for plant_id, plant in cart.items():
        plant_model = get_object_or_404(Plant, pk=plant_id)

        cart_item = {
            "name": plant_model.name,
            # because Stripe deals only with cents
            "amount": int(plant_model.price * 100),
            "quantity": plant['qty'],
            "currency": "SGD"
        }

        cart_items.append(cart_item)

        # store a record to remember that for a given book id,
        # what is the quantity ordered
        all_plant_ids.append({
            'plant_id': plant_id,
            'qty': plant['qty']
        })


    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=cart_items,
        client_reference_id=request.user.id,
        metadata={
            "all_plant_ids": json.dumps(all_plant_ids)
        },
        mode="payment",
        success_url=settings.STRIPE_SUCCESS_URL,
        cancel_url=settings.STRIPE_CANCEL_URL
    )

    # remove all items from the shopping cart
    request.session['shopping_cart'] = {}

    return render(request, 'checkout/checkout-template.html', {
        'session_id': session.id,
        'public_key': settings.STRIPE_PUBLISHABLE_KEY
    })


def checkout_completed(request):

    return render(request, "checkout/order_completed-template.html")


def checkout_not_completed(request):

    return render(request, "checkout/order_not_completed-template.html")

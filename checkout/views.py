from django.shortcuts import render, reverse, HttpResponse, get_object_or_404
from django.conf import settings
import stripe
from products.models import Plant
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib import auth
from checkout.models import Order
from django.contrib.auth.models import User
from django.db.models import Q


# Create your views here.


@login_required
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
            'qty': plant['qty'],
            'price': plant['price'],
            'user': request.user.id
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


@login_required
def order_completed(request):

    return render(request, "checkout/order_completed-template.html")


@login_required
def order_not_completed(request):

    return render(request, "checkout/order_not_completed-template.html")

# To exempt the payment completed function from CSRF


@csrf_exempt
def payment_completed(request):

    payload = request.body

    signature_header = request.META['HTTP_STRIPE_SIGNATURE']

    # To store the data that stripe is sending back to server
    event = None

    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET

    try:
        event = stripe.Webhook.construct_event(
            payload, signature_header, endpoint_secret
        )

    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # means the data is not from Stripe
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':

        plants = Plant.objects.all()

        hours = 8

        hours_added = datetime.timedelta(hours=hours)

        session = event['data']['object']
        session_created = datetime.datetime.fromtimestamp(
            event['created']) + hours_added

        all_plant_ids_jsonstr = session['metadata']['all_plant_ids']

        all_plant_ids = json.loads(all_plant_ids_jsonstr)

        for item in all_plant_ids:

            plant_model = get_object_or_404(Plant, pk=item['plant_id'])
            user_model = get_object_or_404(User, pk=item['user'])

            plant_model.qty = plant_model.qty - item['qty']

            plant_model.save(update_fields=["qty"])

            order = Order(
                title=plant_model.name, price=float(item['price']),
                datetime_ordered=session_created, plant=plant_model,
                order_by=user_model, qty=item['qty'])

            order.save()

    return HttpResponse(status=200)

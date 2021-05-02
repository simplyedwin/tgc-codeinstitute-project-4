from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages
from products.models import Plant
from decimal import Decimal


# Create your views here.

def add_to_cart(request, plant_id):

    # retrieve shopping cart from session
    cart = request.session.get('shopping_cart', {})

    plant = get_object_or_404(Plant, pk=plant_id)

    if plant_id in cart:

        cart[plant_id]['qty'] += 1

    else:

        cart[plant_id] = {

            'id': plant_id,
            'image': str(plant.image),
            'name': plant.name,
            'price': float(plant.price),
            'qty': 1

        }

    request.session['shopping_cart'] = cart

    messages.success(request, "A plant has been added to your shopping cart")

    return redirect(reverse('shop_page'))


def remove_from_cart(request, plant_id):

    cart = request.session.get('shopping_cart', {})

    if plant_id in cart:

        del cart[plant_id]

        request.session['shopping_cart'] = cart

        messages.success(request, "The item has been removed from the cart.")

    return redirect(reverse('view_cart'))


def view_cart(request):

    cart = request.session.get('shopping_cart')

    return render(request, 'cart/view_cart-template.html', {
        'cart': cart
    })

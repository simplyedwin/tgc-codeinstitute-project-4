from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages
from products.models import Plant
from decimal import Decimal
from Project import settings

# Create your views here.

# this view is to add item to the cart


def add_to_cart(request, plant_id):

    # retrieve shopping cart from session
    cart = request.session.get('shopping_cart', {})

    # retrieve all plant info
    plant = get_object_or_404(Plant, pk=plant_id)
    unit_price = plant.price

    # to update the cart line items
    if plant_id in cart:

        cart[plant_id]['qty'] += 1
        cart[plant_id]['price'] = float(
            unit_price) * cart[plant_id]['qty']

    else:

        # crearte the cart line items
        cart[plant_id] = {

            'id': plant_id,
            'image': str(plant.image),
            'name': plant.name,
            'price': float(plant.price),
            'qty': 1

        }

    # to create the cart during session
    request.session['shopping_cart'] = cart

    messages.success(request, "A plant has been added to your shopping cart")

    return redirect(reverse('shop_page'))

# this view is to remove item from the cart


def remove_from_cart(request, plant_id):

    # retrieve the cart at current session
    cart = request.session.get('shopping_cart', {})

    # to remove the cart for the requested plant
    if plant_id in cart:

        del cart[plant_id]

        request.session['shopping_cart'] = cart

        messages.success(request, "The item has been removed from the cart.")

    return redirect(reverse('view_cart'))

# this view is to update item in the cart


def update_cart(request, plant_id):

    plant = get_object_or_404(Plant, pk=plant_id)
    unit_price = plant.price

    # retrive the shopping cart from session
    cart = request.session.get('shopping_cart', {})
    if plant_id in cart:
        cart[plant_id]['qty'] = int(request.POST['qty'])
        cart[plant_id]['price'] = float(
            unit_price) * int(request.POST['qty'])

        request.session['shopping_cart'] = cart
        messages.success(
            request, 'The quantity for the item has been updated.')

    return redirect(reverse('view_cart'))

# this view is to display the cart info


def view_cart(request):

    cart = request.session.get('shopping_cart')

    total_sum = 0

    if cart is not None:

        for item in cart:

            item_total = (cart[item]['price']/cart[item]
                          ['qty']) * cart[item]['qty']

            total_sum = total_sum + item_total

    return render(request, 'cart/view_cart-template.html', {
        'cart': cart,
        'total_sum': total_sum
    })

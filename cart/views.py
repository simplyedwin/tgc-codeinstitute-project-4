from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages
from products.models import Plant
import json
from decimal import Decimal


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)


# Create your views here.

def add_to_cart(request, plant_id):

    # retrieve shopping cart from session
    cart = request.session.get('shopping_cart', {})

    plant = get_object_or_404(Plant, pk=plant_id)

    cart[plant_id] = {

        'id': plant_id,
        'name': plant.name,
        'price': json.dumps(plant.price, cls=DecimalEncoder),  # plant.price,
        'qty': 1

    }

    request.session['shopping_cart'] = cart

    messages.success(request, "A plant has been added to your shopping cart")

    return redirect(reverse('shop_page'))


def view_cart(request):

    cart = request.session.get('shopping_cart')

    return render(request, 'cart/view_cart-template.html', {
        'cart': cart
    })


# def post_flash_msg(request):

#     django_messages = []

#     for message in messages.get_messages(request):
#         django_messages.append({
#             "level": message.level,
#             "message": message.message,
#             "extra_tags": message.tags,
#         })

#     data = []

#     # data['success'] = success
#     data.append(django_messages)

#     # serialize in new friend object in json
#     ser_instance = serializers.serialize('json', data)
#     # send to client side.
#     return JsonResponse({success: ser_instance}, status=200)

#     # return HttpResponse(json.dumps(data), content_type="application/json")

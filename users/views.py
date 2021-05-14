from products.models import Plant
from django.shortcuts import redirect, render, reverse
from .forms import UserForm, UserInfoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, update_session_auth_hash, login
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from checkout.models import Order
from django.db.models import Q
from reviews.models import Review
from products.views import shop_page

# Create your views here.

# this view require login and for user to edit
# profile information and view order history


@login_required
def user_account(request):

    # to determine the qty of items in cart
    cart = request.session.get('shopping_cart', {})

    # to retrieve review status
    reviewed_order_ids = []

    # to pass the reviewed order id
    reviewed_order_ids_dict = {}

    # to retrieve the current user
    user = request.user

    # to retrieve all the reviews
    reviews = Review.objects.all()

    # to retrieve all the plants
    plants = Plant.objects.all()

    # to retrieve all the orders
    orders = Order.objects.all()

    # to filter the orders by current user
    query = Q(order_by__exact=user)

    # to retrieve all the orders for the current user
    orders = orders.filter(query).values().distinct()

    # to retreive all the reviews id if true
    if reviews:
        for review in reviews:

            reviewed_order_ids.append(review.order.id)

    reviewed_order_ids_dict["reviewed_order_ids"] = reviewed_order_ids

    if request.method == 'POST':

        user_form = UserForm(request.POST, instance=request.user)
        userinfo_form = UserInfoForm(
            request.POST, instance=request.user.userinfo)
        password_change_form = PasswordChangeForm(request.user, request.POST)
        # save the content of the form if it is valid
        if (user_form.is_valid() and userinfo_form.is_valid()
                and password_change_form.is_valid()):
            user = password_change_form.save()
            update_session_auth_hash(request, user)
            user_form.save()
            userinfo_form.save()
            messages.success(request,
                             'Your profile was successfully updated!')
            return redirect(reverse(user_account))
        else:

            # sent flash error message and ask user to correct the fields
            messages.error(request, 'Please correct the error below.')
            return render(request, 'users/user_info-template.html', {
                'user_form': user_form,
                'userinfo_form': userinfo_form,
                'password_change_form': password_change_form,
                'orders': orders,
                "reviewed_plant_order_ids_dict": reviewed_order_ids_dict,
                "reviews": reviews,
                'plants': plants
            })

    else:
        user_form = UserForm(instance=request.user)
        userinfo_form = UserInfoForm(instance=request.user.userinfo)
        password_change_form = PasswordChangeForm(request.user)

    return render(request, 'users/user_info-template.html', {
        'user_form': user_form,
        'userinfo_form': userinfo_form,
        'password_change_form': password_change_form,
        'orders': orders,
        "reviewed_plant_order_ids_dict": reviewed_order_ids_dict,
        "reviews": reviews,
        'plants': plants,
        'cart': cart
    })

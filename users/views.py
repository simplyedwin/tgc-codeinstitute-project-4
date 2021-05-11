from django.shortcuts import redirect, render, reverse
from .forms import UserForm, UserInfoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from checkout.models import Order
from django.db.models import Q
from reviews.models import Review

# Create your views here.


def contact_us(request):

    return render(request, 'users/contact_us-template.html')


@login_required
def user_account(request):

    # to retrieve review status
    reviewed_plant_ids = []

    reviewed_plant_dict = {}

    # to retrieve the current user
    user = request.user

    # to retrieve all the reviews
    reviews = Review.objects.all()

    # to retrieve all the orders
    orders = Order.objects.all()

    # to filter the orders by current user
    query = Q(order_by__exact=user)

    # to retrieve all the orders for the current user
    orders = orders.filter(query).values().distinct()

    if reviews:
        for review in reviews:
            reviewed_plant_ids.append(review.plant.id)

        reviewed_plant_dict["plant_ids"] = reviewed_plant_ids

    print(reviewed_plant_dict)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        userinfo_form = UserInfoForm(
            request.POST, instance=request.user.userinfo)
        password_change_form = PasswordChangeForm(request.user, request.POST)
        if (user_form.is_valid() and userinfo_form.is_valid()
                and password_change_form.is_valid()):
            user = password_change_form.save()
            update_session_auth_hash(request, user)  # Important!
            user_form.save()
            userinfo_form.save()
            messages.success(request,
                             'Your profile was successfully updated!')
            return redirect(reverse(user_account))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        userinfo_form = UserInfoForm(instance=request.user.userinfo)
        password_change_form = PasswordChangeForm(request.user)

    return render(request, 'users/user_info-template.html', {
        'user_form': user_form,
        'userinfo_form': userinfo_form,
        'password_change_form': password_change_form,
        'orders': orders,
        "reviewed_plant_dict": reviewed_plant_dict,
        "reviews": reviews
    })

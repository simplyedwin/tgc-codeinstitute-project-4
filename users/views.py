from django.shortcuts import redirect, render, reverse
from .forms import UserForm, UserInfoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.


@login_required
def user_account(request):

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        userinfo_form = UserInfoForm(
            request.POST, instance=request.user.userinfo)
        password_change_form = PasswordChangeForm(request.user, request.POST)
        if user_form.is_valid() and userinfo_form.is_valid() and password_change_form.is_valid():
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
        'password_change_form': password_change_form
    })

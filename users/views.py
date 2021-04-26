from django.shortcuts import redirect, render
from .forms import UserForm, UserInfoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def user_account(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        userinfo_form = UserInfoForm(
            request.POST, instance=request.user.userinfo)
        if user_form.is_valid() and userinfo_form.is_valid():
            user_form.save()
            userinfo_form.save()
            messages.success(request,
                             'Your profile was successfully updated!')
            return redirect('settings:profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        userinfo_form = UserInfoForm(instance=request.user.userinfo)
    return render(request, 'users/user_info-template.html', {
        'user_form': user_form,
        'userinfo_form': userinfo_form
    })

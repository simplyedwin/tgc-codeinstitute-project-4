from django.shortcuts import render

# Create your views here.


def login_signup(request):
    return render(request, 'users/login_signup-template.html')

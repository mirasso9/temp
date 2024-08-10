from django.shortcuts import render

# Create your views here.
# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.user.is_authenticated:
        return redirect('user_dashboard')  # Redirect to user dashboard if already logged in

    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        # Here, you should have logic to authenticate using the phone number.
        # If phone number is being used as the username, ensure your user model supports it.

        user = authenticate(request, username=phone, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('user_dashboard')
        else:
            messages.error(request, 'Invalid phone number or password.')

    return render(request, 'accounts/login.html')


def index(request):
    return render(request, 'main/footer.html')

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Listing


from django.shortcuts import render
from .forms import UserForm


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'listings/login.html')
    else:
        listings = Listing.objects.filter(user=request.user)
        return render(request, 'listings/index.html', {'listings': listings})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Listing.objects.filter(user=request.user)
                return render(request, 'listings/index.html', {'albums': albums})
            else:
                return render(request, 'listings/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'listings/login.html', {'error_message': 'Invalid login'})
    return render(request, 'listings/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Listing.objects.filter(user=request.user)
                return render(request, 'listings/index.html', {'albums': albums})
    context = {
        "form": form,
    }
    return render(request, 'listings/register.html', context)

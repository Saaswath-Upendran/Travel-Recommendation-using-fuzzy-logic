from django.shortcuts import render, redirect
from .forms import UserForm, UserProfile, BookingForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Travel, Booking, Hotel
import datetime
from django.contrib import messages
from django.db.models import Q
from django.http import Http404
from django.db.models import Case, When
import pandas as pd
import numpy as np
from .recommendation import Myrecommend
# Create your views here.


def Home(request):
    template_name = 'sample.html'
    return render(request, template_name, {})


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfile(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfile()

    return render(request, 'register.html', {'user_form': user_form, "profile_form": profile_form, "registered": registered})


def user_homepage(request):
    current_user = request.user
    booking_details = Booking.objects.filter(
        user_id_id__in=str(current_user.id))
    return render(request, "userhome.html", {"bookings": booking_details})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('user')

            else:
                return HttpResponse("Account not active")
        else:
            print("Some tried to login and failed")
            print("Username: {} and password :{}".format(username, password))
            return HttpResponse("invalid login details")
    else:
        return render(request, 'login.html', {})


@login_required
def search(request):
    if not request.user.is_authenticated:
        return redirect("user_login")
    if request.method == "POST":
        searched = request.POST['destination']
        checkbox = request.POST.getlist("priority")
        print(checkbox)
        if searched == "jaipur" or "JAIPUR":
            result = Travel.objects.all()
            hotel = Hotel.objects.filter(
                hotel_id__contains=np.random.randint(5))

            if len(checkbox) < 1:
                priority = result.filter(
                    PRIORITY_1__icontains=checkbox)
            else:
                priority = result.filter(
                    PRIORITY_1__in=checkbox)
        return render(request, 'search.html', {"search": searched, "place": priority, "hotel": hotel})

    else:
        return render(request, "search.html")


def AboutUs(request):
    template_name = "about.html"
    return render(request, template_name, {})


@login_required
def booking_site(request, hotel_id):
    hotel = Hotel.objects.get(hotel_id=hotel_id)
    if not request.user.is_authenticated:
        return redirect('user_login')
    booking = False
    if request.method == "POST":
        book = BookingForm(request.POST)
        print(request.user.id)
        book.user_id_id = request.user.id
        print(book["hotel_name"])
        if book.is_valid():
            book.save(commit=False)
            book.save()
            booking = True
            messages.success(request, "Your booking is submited ")
            return redirect('recomendation')
    else:
        book = BookingForm(initial={"hotel_name": hotel})
        current_user = request.user
        

        return render(request, 'booking.html', {"book": book, "booking": booking})


def page_404_page(request, exception):
    return render(request, '404.html', status=404)


@login_required
def recommend(request):
    if not request.user.is_authenticated:
        return redirect("user_login")
    if not request.user.is_active:
        raise Http404
    result = Travel.objects.filter(id__contains=np.random.randint(70))
    print(result)
    return render(request, 'recommendation.html', {"result": result})


@login_required
def delete_booking(request, hotel_id):
    hotel = Booking.objects.filter(hotel_name_id__exact=hotel_id)
    hotel.delete()
    return redirect('userhome')

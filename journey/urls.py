from django.urls import path, re_path
from .views import *

app_name = "journey"
urlpatterns = [

    path('register/', register, name='register'),
    path('login/', user_login, name="user_login"),
    path('logout/', user_logout, name="user_logout"),
    path('aboutus/', AboutUs, name="about"),
    re_path(r'search', search, name='search'),
    path("book/<int:hotel_id>", booking_site, name="book"),
    path("delete/<int:hotel_id>",delete_booking,name="delete_booking")


]

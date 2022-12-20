from django.contrib import admin
from .models import UserProfileInfo, Booking, Hotel, Travel
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Booking)
admin.site.register(Hotel)
admin.site.register(Travel)

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

# Create your models here.


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone_no = models.IntegerField(max_length=10)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username


class Travel(models.Model):
    id = models.CharField(_("id"), primary_key=True, max_length=5)
    POIS = models.TextField(_('POIs'), max_length=255)
    PRIORITY_1 = models.TextField(_("PRIORITY_1"), max_length=255)
    PRIORITY_2 = models.TextField(_("PRIORITY_2"), max_length=255)
    PRIORITY_3 = models.TextField(_("PRIORITY_3"), max_length=255)
    PRIORITY_4 = models.TextField(_("PRIORITY_4"), max_length=255)
    PRIORITY_5 = models.TextField(_("PRIORITY_5"), max_length=255)
    PLACE_LOGO = models.FileField()

    def __str__(self):
        return self.PRIORITY_1


class Hotel(models.Model):
    hotel_id = models.TextField(_('hotel_id'), primary_key=True, max_length=5)
    name = models.TextField(_('HOTEL'), max_length=120)
    price = models.IntegerField(_('PRICE_RUPEES'), max_length=12)
    Number_of_reviews = models.TextField(
        _('NUMBER_OF_REVIEWS'), max_length=125)
    Lat = models.IntegerField(_('Lat'), max_length=20)
    Lng = models.IntegerField(_('Lng'), max_length=20)
    Hote_logo = models.FileField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    choicies = (('1', '1'),
                ('2', '2'),
                ('3', '3'),
                ('4', '4'),
                ('5', '5'),
                ('6', '6'),
                ('7', '7'),
                ('8', '8'),
                ('9', '9'),
                ('10', '10')
                )

    booking_person = models.CharField(choices=choicies, max_length=12)
    hotel_name = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    date_in = models.DateField(
        max_length=12, null=True, blank=True)
    date_out = models.DateField(
        max_length=12, null=True, blank=True)

    def __str__(self):
        return self.hotel_name.name

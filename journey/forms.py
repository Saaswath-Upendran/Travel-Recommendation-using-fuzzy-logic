from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo, Booking, Hotel


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password')


class UserProfile(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('email', 'phone_no', 'profile_pic')


class BookingForm(forms.ModelForm):
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
    booking_person = forms.ChoiceField(choices=choicies)

    class Meta():
        model = Booking
        fields = ('user_id', 'booking_person','hotel_name','date_in', 'date_out')
        widgets = ({
            "date_in": forms.DateInput(attrs={'id': 'datepicker'}),
            "date_out": forms.DateInput(attrs={'id': 'datepicker1'})
        })

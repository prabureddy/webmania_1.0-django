from django import forms
from django.core import validators
from index.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class Shedule_Ride_Form(forms.ModelForm):

    class Meta:
        model = Shedule_Ride
        fields = '__all__'

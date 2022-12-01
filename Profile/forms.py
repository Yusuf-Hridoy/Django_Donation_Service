from django import forms
from django.forms import ModelForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Volunteer


class SignUp(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name', 'email', 'password1', 'password2']



class BecomeVolunteerForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name', 'email', 'password1', 'password2']

# class Userform(forms.ModelForm):
#     firstname= forms.CharField(widget= forms.TextInput
#                            (attrs={'placeholder':'Enter your first name'}))
#     email= forms.CharField(widget= forms.EmailInput
#                            (attrs={'placeholder':'Enter your email'}))
#     phonenumber= forms.CharField(widget= forms.TextInput
#                            (attrs={'placeholder':'(xxx)xxx-xxxx'}))
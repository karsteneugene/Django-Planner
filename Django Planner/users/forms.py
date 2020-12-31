from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


# Uses the User model so the new user will be added to the table
class UserRegisterForm(UserCreationForm):
    # Added an email field for registration
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Uses the User model so the logged in users will be able to update their information
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


# Uses the Profile model so the logged in users will be able to edit their profile picture
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

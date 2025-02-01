# forms.py
from django import forms
from .models import HouseHelp, Employer

from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class HouseHelpRegistrationForm(forms.ModelForm):
    class Meta:
        model = HouseHelp
        fields = ['username', 'password', 'email', 'phone_number', 'first_name', 'last_name', 'location',
                  'job_titles', 'experience', 'references', 'availability', 'rate', 'background_check',
                  'profile_picture']
        widgets = {
            'password': forms.PasswordInput(),
            'background_check': forms.ClearableFileInput(attrs={'multiple': False}),
            'profile_picture': forms.ClearableFileInput(attrs={'multiple': False}),
        }


class EmployerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ['username', 'password', 'email', 'phone_number', 'first_name', 'last_name', 'location',
                  'number_of_people', 'specific_needs', 'frequency_of_service', 'profile_picture']
        widgets = {
            'password': forms.PasswordInput(),
            'profile_picture': forms.ClearableFileInput(attrs={'multiple': False}),
        }


# forms.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

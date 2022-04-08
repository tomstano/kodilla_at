from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    CHOICES = [("student", "Student"), ("instructor", "Instructor")]
    usertype = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ["username", "email", "usertype", "password1", "password2"]

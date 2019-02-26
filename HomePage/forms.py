from django import forms
from django.contrib.auth.models import User
from UserPage.models import UserProfile

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'password', 'email')

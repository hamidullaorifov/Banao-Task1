from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegisterForm(UserCreationForm):
    # profile_picture = forms.ImageField()
    # password1 = forms.CharField(validators=[])
    # password2 = forms.CharField(validators=[])
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'profile_picture',
            'email',
            'username',
            'type',
            'line1',
            'city',
            'state',
            'pincode',
            )

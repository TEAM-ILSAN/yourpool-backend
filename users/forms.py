from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import YourPoolUser

class YourPoolUserCreationForm(UserCreationForm):
    
    class Meta:
        model = YourPoolUser
        fields = ("username", "email")

class YourPoolUserChangeForm(UserChangeForm):

    class Meta:
        model = YourPoolUser
        fields = ("username", "email")
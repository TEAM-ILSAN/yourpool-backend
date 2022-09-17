from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import YourPoolUserChangeForm, YourPoolUserCreationForm
from .models import YourPoolUser


class YourPoolUserAdmin(UserAdmin):
    add_form = YourPoolUserCreationForm
    form = YourPoolUserChangeForm
    model = YourPoolUser
    list_display = ["email", "username"]


admin.site.register(YourPoolUser, YourPoolUserAdmin)

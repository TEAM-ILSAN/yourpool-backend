from django.contrib import admin
from users.models import YourPoolUser


class YourPoolUserAdmin(admin.ModelAdmin):
    list_display = ("email", "nickname", "gender", "area", "is_email_verified")


admin.site.register(YourPoolUser, YourPoolUserAdmin)

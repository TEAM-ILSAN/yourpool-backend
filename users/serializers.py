from .models import YourPoolUser

from rest_framework import serializers

from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = YourPoolUser
        fields = (
            "email",
            "nickname",
            "password",
            "area",
            "gender",
            "is_email_verified",
        )


class VerifyAccountSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()
    
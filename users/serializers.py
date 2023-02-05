import re

from .models import YourPoolUser

from rest_framework import serializers

from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string


class SignupSerializer(serializers.ModelSerializer):

    password = serializers.CharField(min_length=8, write_only=True)
    
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

    def validate_password(self, data):
        
        PASSWORD_VALIDATION = re.compile('(?=.{8,})(?=.*[a-zA-Z!@#$%^&*()_+~])(?=.*[!@#$%^&*()_+~0-9]).*')

        if not PASSWORD_VALIDATION.match(data):
            raise serializers.ValidationError(
                "more than eight digits, Please include at least two English/numeric/symbols."
            )
        
        return data 
    
    def create(self, validate_data):
        return YourPoolUser.objects.create_user(**validate_data)


class LogininSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = YourPoolUser
        fields = (
            "email",
            "password",
            "token",
            "is_email_verified",
        )
        read_only_fields=['token']

class VerifyAccountSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()
    
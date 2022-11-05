from rest_framework import serializers

from .models import YourPoolUser


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = YourPoolUser
        fields = ("email", "username", "password", "password2", "area", "gender")

    def validate(self, args):
        email = args.get("email", None)
        username = args.get("username", None)

        if YourPoolUser.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": ("email already exists")})

        if YourPoolUser.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {"username": ("user name already exists")}
            )

        return super().validate(args)

    def create(self, validated_data):
        return YourPoolUser.objects.create_user(**validated_data)

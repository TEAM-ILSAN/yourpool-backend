from rest_framework import serializers

from .models import YourPoolUser


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = YourPoolUser
        fields = ("email", "username", "password", "area", "gender")

    # client가 입력한 email과 username을 받고 데이터베이스 존재 유무를 판단해 에러를 처리한다.
    # 만약 존재하지 않는다면 유저를 생성한다.
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

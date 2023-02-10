import jwt

from django.contrib.auth import authenticate

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework import status

from smtplib import SMTPException

from .serializers import SignupSerializer, VerifyAccountSerializer, LogininSerializer
from .emails import send_otp_via_email
from .models import YourPoolUser


class SignupView(GenericAPIView):
    serializer_class = SignupSerializer

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                send_otp_via_email(serializer.data["email"])
                return Response(
                    {
                        "status": 201,
                        "message": "registration successfully check email",
                        "data": serializer.data,
                    }
                )
            return Response(
                {
                    "status": 400,
                    "message": "something went wrong",
                    "data": serializer.errors,
                }
            )
        except SMTPException as e:
            return Response(
                {
                    "status": e.smtp_code,
                    "message": e.smtp_error,
                    "data": serializer.errors,
                }
            )


class VerifyOTP(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = VerifyAccountSerializer(data=data)

            if serializer.is_valid():
                email = serializer.data["email"]
                otp = serializer.data["otp"]

                user = YourPoolUser.objects.filter(email=email)
                if not user.exists():
                    return Response(
                        {
                            "status": 400,
                            "message": "something went wrong",
                            "data": "invalid email",
                        }
                    )

                if user[0].otp != otp:
                    return Response(
                        {
                            "status": 400,
                            "message": "something went wrong",
                            "data": "wrong otp",
                        }
                    )
                user = user.first()
                user.is_email_verified = True
                user.save()

                return Response(
                    {
                        "status": 200,
                        "message": "account verified",
                        "data": {},
                    }
                )
            return Response(
                {
                    "status": 400,
                    "message": "something went wrong",
                    "data": serializer.errors,
                }
            )
        except Exception as e:
            print(e)


class LoginView(GenericAPIView):
    serializer_class = LogininSerializer

    def post(self, request):
        email = request.data.get("email", None)
        password = request.data.get("password", None)

        user = authenticate(username=email, password=password)

        if user and user.is_email_verified:
            serializer = self.serializer_class(user)

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(
            {"message": "Invalid credentials, try again"},
            status=status.HTTP_401_UNAUTHORIZED,
        )

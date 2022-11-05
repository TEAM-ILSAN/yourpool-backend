import json, uuid

from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from validate_email import validate_email
from rest_framework import generics, status, serializers
from rest_framework.response import Response

from users.serializers import SignupSerializer

from .models import YourPoolUser


class SignupView(generics.GenericAPIView):
    serializer_class = SignupSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "RequestId": str(uuid.uuid4()),
                    "Message": "User created successfully",
                    "User": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"errors": serializers.errors}, status=status.HTTP_400_BAD_REQUEST
        )


# @method_decorator(csrf_exempt, name="dispatch")
# class Register(View):
#     def post(self, request):
#         try:
#             data = json.loads(request.body)

#             email = data["email"]
#             username = data["username"]
#             gender = data["gender"]
#             area = data["area"]
#             password = data["password"]
#             password2 = data["password2"]

#             # Error when password is less than 8 characters
#             if len(password) < 8:
#                 messages.add_message(
#                     request, messages.ERROR, "Password should be at least 6 characters"
#                 )
#                 return JsonResponse({"message": "PASSWORD_LENGTH_ERROR"}, status=401)

#             # Confirm password
#             if password != password2:
#                 messages.add_message(request, messages.ERROR, "Password mismatch")
#                 return JsonResponse(
#                     {"message": "CONFIRMATION_PASSWORD_MISMATCH"}, status=401
#                 )

#             if not validate_email(email):
#                 messages.add_message(
#                     request, messages.ERROR, "Enter a valid email address"
#                 )
#                 return JsonResponse({"message": "EMAIL_FORMAT_ERROR"}, status=401)

#             # Error when user name alreay exists
#             if YourPoolUser.objects.filter(username=username).exists():
#                 messages.add_message(
#                     request, messages.ERROR, "Username is taken, choose another one"
#                 )
#                 return JsonResponse({"message": "USERNAME_ALREADY_EXIST"}, status=400)

#             # Error when email alreay exists
#             if YourPoolUser.objects.filter(email=email).exists():
#                 messages.add_message(
#                     request, messages.ERROR, "Email is taken, choose another one"
#                 )
#                 return JsonResponse({"message": "EMAIL_ALREADY_EXIST"}, status=400)

#             if not gender == "F":
#                 if gender == "M":
#                     return JsonResponse({"message": "ONLY_WOMEN_CAN_JOIN"}, status=400)
#                 else:
#                     return JsonResponse(
#                         {"message": "GENDER_FORMAT_INCORRECT"}, status=400
#                     )

#             user = YourPoolUser.objects.create_user(
#                 username=username, email=email, gender=gender, area=area
#             )
#             user.set_password(password)
#             user.save()

#             messages.add_message(
#                 request, messages.SUCCESS, "Account created, you can now login"
#             )
#             return JsonResponse({"message": "REGISTER_SUCCESS"}, status=201)

#         except KeyError:
#             return JsonResponse({"message": "KEY_ERROR"}, status=400)

#         except json.decoder.JSONDecodeError:
#             return JsonResponse({"MESSAGE": "JSONDecodeError"}, status=400)


# @method_decorator(csrf_exempt, name="dispatch")
# class Signin(View):
#     def post(self, request):
#         try:
#             data = json.loads(request.body)

#             email = data["email"]
#             password = data["password"]

#             if not YourPoolUser.objects.filter(email=email).exists():


#             return JsonResponse({"message": "SIGNIN_SUCCESS"}, status=200)

#         except KeyError:
#             return JsonResponse({"message": "KEY_ERROR"}, status=400)

#         except json.decoder.JSONDecodeError:
#             return JsonResponse({"MESSAGE": "JSONDecodeError"}, status=400)

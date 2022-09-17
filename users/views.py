import requests

from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework import permissions

from moiza.settings import SOCIAL_OUTH_CONFIG
from .models import User

# class KaKaoLoginView(APIView):
#     permission_classes = [permissions.AllowAny]

#     def get(self, request):
#         app_key = SOCIAL_OUTH_CONFIG['KAKAO_REST_API_KEY']
#         redirect_uri = SOCIAL_OUTH_CONFIG['KAKAO_REDIRECT_URI']
#         kakao_auth_api = "https://kauth.kakao.com/oauth/authorize?response_type=code"

#         return redirect(
#             "{kakao_auth_api}&client_id={app_key}&redirect_uri={redirect_uri}".format(
#                 kakao_auth_api=kakao_auth_api, app_key=app_key, redirect_uri=redirect_uri)
#         )


# def kakao_callback(request):
#     auth_code = request.GET.get('code')
#     kakao_token_api = "https://kauth.kakao.com/oauth/token"
#     data = {
#         'grant_type': 'authorization_code',
#         'client_id': SOCIAL_OUTH_CONFIG['KAKAO_REST_API_KEY'],
#         'redirect_url': SOCIAL_OUTH_CONFIG['KAKAO_REDIRECT_URI'],
#         'client_secret': SOCIAL_OUTH_CONFIG['KAKAO_SECRET_KEY'],
#         'code': auth_code
#     }

#     token_response = requests.post(kakao_token_api, data=data)

#     access_token = token_response.json().get('access_token')

#     user_info_response = requests.get("https://kapi.kakao.com/v2/user/me", headers={
#         "Authorization": "Bearer {access_token}".format(access_token=access_token)})

#     json_kakao_user_info = user_info_response.json()

#     # Get user information
#     user_kakao_email = json_kakao_user_info["kakao_account"]["email"]
#     user_kakao_nickname = json_kakao_user_info["kakao_account"]["profile"]["nickname"]
#     kakao_id = json_kakao_user_info["id"]

#     # Saving user information to a database
#     # If there is no user gender information, save as null
#     try:
#         User.objects.get(email=user_kakao_email)
    
#     except User.DoesNotExist:
#         if json_kakao_user_info["kakao_account"]["has_gender"] == True:
#             gender = json_kakao_user_info["kakao_account"]["gender"]
            
#             User.objects.create(
#                 kakao_id=kakao_id,
#                 email=user_kakao_email,
#                 nickname=user_kakao_nickname,
#                 gender=gender
#             )
#         else:
#             User.objects.create(
#                 kakao_id=kakao_id,
#                 email=user_kakao_email,
#                 nickname=user_kakao_nickname
#             )

#     return JsonResponse({"user_info": user_info_response.json(), "access_token": access_token})
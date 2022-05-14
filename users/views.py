import requests

from django.http import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import authentication, permissions


from moiza.settings import SOCIAL_OUTH_CONFIG


def empty(request):
    return render(request, 'users/empty.html')


class KaKaoLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        app_key = SOCIAL_OUTH_CONFIG['KAKAO_REST_API_KEY']
        redirect_uri = SOCIAL_OUTH_CONFIG['KAKAO_REDIRECT_URI']
        kakao_auth_api = "https://kauth.kakao.com/oauth/authorize?response_type=code"

        return redirect(
            "{kakao_auth_api}&client_id={app_key}&redirect_uri={redirect_uri}".format(
                kakao_auth_api=kakao_auth_api, app_key=app_key, redirect_uri=redirect_uri)
        )


class KaKaoLoginCallBackView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        auth_code = request.GET.get('code')
        kakao_token_api = "https://kauth.kakao.com/oauth/token"
        data = {
            'grant_type': 'authorization_code',
            'client_id': SOCIAL_OUTH_CONFIG['KAKAO_REST_API_KEY'],
            'redirect_url': SOCIAL_OUTH_CONFIG['KAKAO_REDIRECT_URI'],
            'client_secret': SOCIAL_OUTH_CONFIG['KAKAO_SECRET_KEY'],
            'code': auth_code
        }

        token_response = requests.post(kakao_token_api, data=data)

        access_token = token_response.json().get('access_token')

        print(access_token)

        user_info_response = requests.get("https://kapi.kakao.com/v2/user/me", headers={
            "Authorization": "Bearer {access_token}".format(access_token=access_token)})

        return JsonResponse({"user_info": user_info_response.json()})

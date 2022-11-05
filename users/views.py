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
        # 유저 정보가 이미 존재하는 지 아닌지 판단
        serializer = self.get_serializer(data=request.data)
        # 유저 정보가 존재하지 않는다면 새로운 유저를 만드는데 성공한다.
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "request_id": str(uuid.uuid4()),
                    "message": "User created successfully",
                    "user": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"errors": serializers.errors}, status=status.HTTP_400_BAD_REQUEST
        )



# 위치값 저장 (req = 위도, 경도, 유저번호 / ret = true, false)
def updategeo(request):

    # url에서 받는 정보 
    req_lat = request.GET.get('lat')
    req_lon = request.GET.get('lon')
    req_uid = request.GET.get('uid')
    
    # 카카오 id로 조회한 유저의 값(젠더, 주소)를 저장 (update)
    kakao_user = YourPoolUser.objects.get(id=req_uid)
    YourPoolUser.lat = req_lat
    kakao_user.lon = req_lon
    kakao_user.save()
    
    # 저장이 잘 되었는지 확인
    checkUser = YourPoolUser.objects.get(id=req_uid)         
    print(type(checkUser.lon))
    print(type(req_lon))

    if(str(checkUser.lon) in req_lon):
        rt = "true"
    else:
        rt = "false"

    return JsonResponse({"rt":rt}) 



class LoginView(generics.GenericAPIView):
    def post(self, request):

        data = json.loads(request.body)

        email = data["email"]
        password = data["password"]

        user = authenticate(request, email=email, password=password)

        if not user:
            messages.add_message(request, messages.ERROR, "invalid credentails")
            return Response(
                {"message": "invalid credentails"}, status=status.HTTP_401_UNAUTHORIZED
            )

        return Response({"message": "login success"}, status=status.HTTP_200_OK)

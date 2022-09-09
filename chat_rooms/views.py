# from asyncio.windows_events import NULL
from copyreg import constructor
from pydoc import describe
from re import L
import string
from turtle import st
from unicodedata import category
from django.shortcuts import render
from .models import ChatRoom
from django.http import JsonResponse
from datetime import datetime, timedelta
# Create your views here.

#http://localhost:8000/chat/newChat/?category=운동&uid=3&lat=33.777777&lon=126.111111&area=백석동&room_name=hi&description=jojo&num_choices=1&limit=3&meet_time=2022-09-10%2013:35:42.657813
def newChat(request):
    category = request.GET.get('category')
    uid = request.GET.get('uid')
    Area = request.GET.get('area')
    Lon = request.GET.get('lon')
    Lat = request.GET.get('lat')
    roomName = request.GET.get('room_name')
    Description = request.GET.get('description')
    limit =  request.GET.get('limit')
    meet_time = request.GET.get('meet_time')

    # now = datetime.now()
    # 만나는 시간으로 추가해줘야 함
    # endTime = now + timedelta(hours=6)  #무조건 만나는 시간(meet_time) + 6시간 뒤 폭파

#  2022-09-10 13:35:42.657813



    datetime_string = meet_time
    datetime_format = "%Y-%m-%d %H:%M:%S.%f"

    meet_time = datetime.strptime(datetime_string, datetime_format)
    print("1 #########################")
    print(meet_time) # 2021-12-31 13:35:42.657813
    endTime = meet_time + timedelta(hours=6)
    print("3 #########################")
    print(endTime)

    if(category == None or uid == None or Area == None or Lon == None or Lat == None or roomName == None or Description  == None or limit == None ):
        rt = "false"
        return JsonResponse({"rt": rt})
    
    #카카오 id로 조회한 유저의 값(젠더, 주소)를 저장 (update)
    newroom = ChatRoom.objects.create(
        kakao_id = uid,
        area = Area,
        lat = Lat,
        lon = Lon,
        room_category = category,
        room_name = roomName,
        description = Description,
        limit = limit,
        status = 1,
        meet_time = meet_time,
        end_time = endTime,
    )

    newroom.save()

    print("room name : "+newroom.room_name)

    checkRoom = ChatRoom.objects.filter(room_name=roomName, kakao_id=uid)
    print(len(checkRoom))
    if(len(checkRoom) < 1):
        rt = "false"
    else:
        print(*checkRoom)
        rt = "true"

    return JsonResponse({"rt": rt})

    
# 나의 위도의 소숫점 2자리까지 일치 +-1 숫자까지 조회하여 반환(44 => 43~45)(req = lod(경도) / ret = 조회한 사람 list, true or false)
#http://localhost:8000/chat/selectRoom/?uid=3
def selectRoom(request):
    req_uid = request.GET.get('uid')    
    req_uid = str(req_uid)
    userinfo =  ChatRoom.objects.filter(kakao_id=req_uid, status=1)
    userLon = 0.0
    count = 0

    for row in userinfo.values():
        lon = row['lon']
        userLon = round(lon, 2)

    userLon = float(userLon)
    if(userLon == 0.0):
        print('flase')
        rt = "false"
        return JsonResponse({"rt": rt, "info":"null"})

    userLon0 = round(userLon-0.01, 2) 
    userLon1 = round(userLon+0.01, 2)
    

    # print(userLon)
    people = list(ChatRoom.objects.values().filter(lon__range=(userLon0, userLon1)).values())
    print(people)
    count = len(people)
    
    if(count >= 1):
        print("true")
        rt = "true"
    else:
        print('flase')
        rt = "false"

    return JsonResponse({"rt": rt, "info":people})
# from asyncio.windows_events import NULL
from copyreg import constructor
import json
from pydoc import describe
from re import L
import string
from turtle import st
from unicodedata import category
from django.shortcuts import render
from .models import ChatRoom
from .models import Chat_log
from django.http import JsonResponse
from datetime import datetime, timedelta
import schedule
import time
from django.utils import timezone
# Create your views here.

# http://localhost:8000/chat/newChat/?category=%EC%9A%B4%EB%8F%99&uid=3&lat=33.777777&lon=126.111111&area=%EB%B0%B1%EC%84%9D%EB%8F%99&room_name=hi&description=jojo&limit=3&meet_time=2023-02-05%2013:35:42.657813
#http://localhost:8000/chat/newChat/?category=운동&uid=3&lat=33.777777&lon=126.111111&area=백석동&room_name=hi&description=jojo&num_choices=1&limit=3&meet_time=2022-09-10%2013:35:42.657813
# 방만들기
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
        user = uid,
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
        chat_member = {'0':uid}
    )

    newroom.save()

    checkRoom = ChatRoom.objects.filter(room_name=roomName, user=uid).values()
    print(checkRoom)
    print(len(checkRoom))
    if(len(checkRoom) < 1):
        rt = "false"
    else:
        print(*checkRoom)
        rt = "true"

    return JsonResponse({"rt": rt})




    
# 나의 위도의 소숫점 2자리까지 일치 +-1 숫자까지 조회하여 반환(1.44 => 1.43 ~ 1.45)(req = uid / ret = 조회한 사람 list, true or false)
#http://localhost:8000/chat/selectRoom/?uid=49
def selectRoom(request):
    req_uid = request.GET.get('uid')    
    req_uid = str(req_uid)
    userinfo =  ChatRoom.objects.filter(user=req_uid, status=1) # 유저 정보 가져오기 위해서 
    userLon = 0.0
    count = 0

    for row in userinfo.values():
        lon = row['lon']
        userLon = round(lon, 2)

    userLon = float(userLon)
    if(userLon == 0.0):
        rt = "false"
        return JsonResponse({"rt": rt, "info":"null"})

    userLon0 = round(userLon-0.01, 2) 
    userLon1 = round(userLon+0.01, 2)
    

    # print(userLon)
    people = list(ChatRoom.objects.values().filter(lon__range=(userLon0, userLon1)).values())
    # print(people)
    count = len(people)
    # print(count)
    if(count >= 1):
        # print("true")
        rt = "true"
    else:
        # print('flase')
        rt = "false"

    return JsonResponse({"rt": rt, "message":people})



# 조회한 채팅방 중에서 채팅방 입장
# http://localhost:8000/chat/intoRoom/?room_id=29&uid=88
def intoRoom(request):
    req_uid = request.GET.get('uid')  
    req_roomid = request.GET.get('room_id')    
    req_uid = str(req_uid)
    

    # 이미 내가 들어간 방이었음 예외처리 하기


    select = ChatRoom.objects.filter(room_id = req_roomid, status=1).values()
    if(len(select)>=1):
        for limit in select.values():
            if(len(limit['chat_member'])<limit['limit']):
                before = limit['chat_member']
                row  = {len(limit['chat_member']):req_uid}
                before.update(row)
                select.update(chat_member = before)
                rt = "true"
            else:
                rt = 'limit error'
    else:
        rt = "room id error"
    
    return JsonResponse({"rt": rt})



# 조회한 유저 채팅방 퇴장
# http://localhost:8000/chat/outRoom/?room_id=29&uid=88
def outRoom(request):
    req_uid = request.GET.get('uid')  
    req_roomid = request.GET.get('room_id')    
    req_uid = str(req_uid)
    
    select = ChatRoom.objects.filter(room_id = req_roomid, status__in=[1,2]).values()

    if(len(select)>=1):
        for limit in select.values():
            before = limit['chat_member']
            bb = {v:k for k,v in before.items()}            # chat_member에서 req_uid를 찾아서 dict에서 제거
            delid = bb.get(req_uid)                         # 없을 경우 예외처리 추가해야 함!!!!!!!!!!!!!!!!
            before.pop(delid)
            select.update(chat_member = before)
            rt = "true"
    else:
        rt = "room select error"
    
    return JsonResponse({"rt": rt})




# 내가 이용중인 채팅방 리스트
# http://localhost:8000/chat/chatList/?uid=2
def chatList(request):
    req_uid = request.GET.get('uid')  
    # req_uid = str(req_uid)
    # chat_member에 uid 포함 + status = 1,2인 리스트 출력 해야함!!!!!!!! 밑은 테스트 용이라서 3임           //  chat_member__contains={'1':req_uid} 여기를 최대 인원수까지 설정하면 됨
    select = ChatRoom.objects.filter(status__in=[1,2],user=req_uid).values() | ChatRoom.objects.filter(status__in=[1,2],chat_member__contains={'1':req_uid}).values()
    print(select)
    if(len(select)>=1):
        info =[]
        for rooms in select.values():
            info.append(rooms)
            # print(rooms['room_id'])
            rt = 'true'
    else:
        rt = "room search error"
    
    return JsonResponse({"rt": rt, "message": info} )         # 조회된 방 정보 리턴에 담아줘야 함








####################    다음주에 할 일
####################    1. 기존 기능 확인하기. 내가 이용중인 채팅방 리스트 완성하기. 주석 확인하고 조치만 하면 됨. (이용중인 채팅방 리스트 완성도 230129 완료)
####################    2. 스케줄링까지 확인하고 api 작성하기 (230129 1차로 입력 완료)



# ==================== 스케줄링 ====================
# 1. 만남시간이 되면 상태값을 2로 변경해준다
# 2. 폭파시간이 되면 상태값을 3로 변경해준다.
# 3. 2의 폭파시간 상태값을 바꿔줄 때 해당 방의 인원들과 방이름 시간을 저장한다.

# def message1():
#     print("스케쥴 실행중...")

#     # 시간 지났으면서 상태가 1인 방 확인 후 출력
#     now = timezone.now()
#     print(now)
#     late = list(ChatRoom.objects.filter(meet_time__lte = now, status=1).values())
#     print("######## meet_tiem 지난 채팅방 목록 시작 ########")
#     print(late)
#     print("######## meet_tiem 지난 채팅방 목록 끝 ########")
#     # 해당 방들 status = 2로 변경 (만남) #업데이트
#     ChatRoom.objects.filter(meet_time__lte = now).update(status=2)
    

#     print('==============')

#     # 폭파 status = 3으로 변경하며 Chat_log에 로그 남기기 => 조회가 이상함 조회가 안돼서 log 저장도 안 됨
#     log_room = list(ChatRoom.objects.filter(end_time__lte = now).exclude(status=2).values())
#     print("######## end_time 지난 채팅방 목록 시작 ########")
#     for log in log_room:
#         print(log['room_id'])
#         newlog = Chat_log.objects.create(
#         room_id = log['room_id'],
#         meet_time = log['meet_time'],
#         chat_member = log['chat_member'],
#         room_name = log['room_name']
#         )
#         newlog.save()
#     print("######## end_time 지난 채팅방 목록 끝 ########")
#     # 해당 방들 status = 3로 변경 (만남) #업데이트
#     ChatRoom.objects.filter(end_time__lte = now).update(status=3)
    
#     # new_users1 = list(ChatRoom.objects.values().filter(meet_time__lte = now, status=1).values())
#     # print("######## new_users 시작 ########")
#     # print(new_users1)
#     # print("######## new_users 끝 ########")

# def message2(text):
#     print(text)

# # 주기 설정 (10분)
# # job1 = schedule.every(10).minutes.do(message1)
# job1 = schedule.every(1).seconds.do(message1)
# job2 = schedule.every(1).seconds.do(message2,'==============')

# while True:
#     schedule.run_pending()
#     time.sleep(1)
    

# ==================== 스케줄링 ====================

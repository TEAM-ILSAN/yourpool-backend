from django.db import models


class ChatRoom(models.Model):
    room_id = models.AutoField(primary_key=True)
    CATEGORY_CHOICES = [
        ('COFFEECHAT', '커피챗'),
        ('SPORT', '운동'),
        ('WALK', '산책'),
        ('ANIMAL', '반려동물'),
        ('HOBBY', '취미모임'),
        ('GAME', '게임'),
        ('STUDY', '스터디'),
        ('DRINK', '술자리'),
        ('FINANCIAL', '재테크'),
        ('CAREER', '커리어'),
        ('INFO', '동네정보'),
        ('FOOD', '밥친구')
    ]

    user = models.CharField(max_length=50,default='')
    area = models.CharField(max_length=50,default='')
    lat = models.DecimalField(max_digits=1000,decimal_places=6, null=True)                  # 위도
    lon = models.DecimalField(max_digits=1000,decimal_places=6, null=True)                  # 경도
    room_category = models.CharField(max_length=15, choices=CATEGORY_CHOICES)
    room_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    num_choices = zip(range(1, 8), range(1, 8))
    limit = models.IntegerField(choices=num_choices, blank=True, null=True)
    status_choices = [
        ('0', 'off'),
        ('1', 'on'),
        ('2', 'start'),                                                                     # start는 만남이 시작되는 방 => 볼 수 없음
    ]
    status = models.IntegerField(choices=status_choices)                                    # 상태
    start_time = models.DateTimeField(auto_now_add=True)                                    # 시작시간
    meet_time = models.DateTimeField()                                                      # 만날시간
    end_time = models.DateTimeField()                                                       # 종료시간
    chat_member = models.JSONField(null=True)                                               # 입장한 유저번호

    class Meta:
        db_table = 'chat_rooms'


class Chat_log(models.Model):   
    room_id = models.IntegerField()                                                         # chat_rooms의 id 값 가져와서 넣기
    meet_time = models.DateTimeField()                                                      # 만난 시간
    chat_member = models.JSONField(null=True)                                               # 입장한 유저번호
    room_name = models.CharField(max_length=50)                                             # 방제목

    class Meta:
        db_table = 'chat_log'

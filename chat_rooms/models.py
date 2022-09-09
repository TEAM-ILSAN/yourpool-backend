from django.db import models


class ChatRoom(models.Model):
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

    # user = models.ManyToManyField("users.User")                                       # 방장번호
    kakao_id = models.CharField(max_length=50)                                          # 방장번호
    area = models.CharField(max_length=50, null=True)                                   # 한글 지역?  / lat과 lon의 차이가 있나? 필요 없으면 지우기 
    lat = models.DecimalField(max_digits=1000,decimal_places=6, null=True)                  # 위도
    lon = models.DecimalField(max_digits=1000,decimal_places=6, null=True)                  # 경도
    room_category = models.CharField(max_length=15, choices=CATEGORY_CHOICES)               # 카테고리
    room_name = models.CharField(max_length=50)                                             # 방제목
    description = models.CharField(max_length=100)                                          # 소개  
    num_choices = zip(range(1, 8), range(1, 8))                                             # ?
    limit = models.IntegerField(choices=num_choices, blank=True, null=True)                 # 폭파시점
    status_choices = [                                                                      # 방상태
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

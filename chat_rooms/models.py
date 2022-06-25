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

    user = models.ManyToManyField("users.user")
    area = models.CharField(max_length=50)
    room_category = models.CharField(max_length=15, choices=CATEGORY_CHOICES)
    room_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    num_choices = zip( range(1,8), range(1,8) )
    limit = models.IntegerField(choices=num_choices, blank=True)
    status_choices = [
        ('0', 'off'),
        ('1', 'on'),
    ]
    status = models.IntegerField(choices=status_choices)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField()
    chat_member = models.JSONField()

    class Meta:
        db_table = 'chat_rooms'


from random import choices
from django.db import models

class Report(models.Model):
    CATEGORY_CHOICES = [
        ('PROFILE', '부적절한 프로필'),
        ('NAME', '부적절한 이름'),
        ('POLITICAL', '정치적 발언'),
        ('CURSE', '욕설'),
        ('SUGGESTIVE', '선정적인 발언'),
        ('FRAUD', '사기'),
        ('ETC', '기타'),
    ]
    report_time = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField()
    report_user_id = models.ForeignKey("users.user", on_delete=models.PROTECT)
    content = models.CharField(max_length=200)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

    class Meta:
        db_table = 'reports'
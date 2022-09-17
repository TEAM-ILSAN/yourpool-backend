from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser


class YourPoolUser(AbstractUser):
    # REQUIRED_FIELDS = ('email', 'username')

    area = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, null=True)
    phone = models.CharField(max_length=20, null=True)
    description = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.username


class UserItem(models.Model):
    user_id = models.ForeignKey('YourPoolUser', on_delete=models.SET_NULL, null=True)
    use_item = ArrayField(models.IntegerField(), size=50)
    have_item = ArrayField(models.IntegerField(), size=50)

    class Meta:
        db_table = 'users_item'

class Authentication(models.Model):
    phone_number = models.CharField('휴대폰 번호', max_length=30)
    auth_number = models.CharField('인증번호', max_length=30)

    class Meta:
        db_table = 'authentications' 
        verbose_name_plural = "휴대폰인증 관리 페이지"

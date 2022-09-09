from django.db import models
from django.contrib.postgres.fields import ArrayField


class User(models.Model):
    kakao_id = models.CharField(max_length=50, unique=True)
    area = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=1000,decimal_places=6, null=True)
    lon = models.DecimalField(max_digits=1000,decimal_places=6, null=True)
    email = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, null=True)
    phone = models.CharField(max_length=20, null=True)
    description = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'users'


class UserItem(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    use_item = ArrayField(models.IntegerField(), size=50)
    have_item = ArrayField(models.IntegerField(), size=50)

    class Meta:
        db_table = 'users_item'

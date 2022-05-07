from django.db import models
from django.contrib.postgres.fields import ArrayField

class User(models.Model):
    SEX_CHOICES = [
        ('W', 'Women'),
        ('M', 'Men'),
    ]

    area = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    phone = models.CharField(max_length=20)
    description = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'users'

class UserItem(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    use_item = ArrayField(models.IntegerField(), size=50)
    have_item = ArrayField(models.IntegerField(), size=50)

    class Meta:
        db_table = 'users_item'
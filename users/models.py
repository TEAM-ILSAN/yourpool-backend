from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser

from .manage import UserManager


class YourPoolUser(AbstractUser):
    GENDER_CHOICES = (("M", "Male"), ("F", "Female"))

    first_name = None
    last_name = None
    username = None

    email = models.EmailField(unique=True)
    is_email_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, null=True, blank=True)
    nickname = models.CharField(max_length=50, default="")
    area = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, default="F")
    description = models.CharField(max_length=100, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class UserItem(models.Model):
    user_id = models.ForeignKey("YourPoolUser", on_delete=models.SET_NULL, null=True)
    use_item = ArrayField(models.IntegerField(), size=50)
    have_item = ArrayField(models.IntegerField(), size=50)

    class Meta:
        db_table = "users_item"


class Authentication(models.Model):
    phone_number = models.CharField("휴대폰 번호", max_length=30)
    auth_number = models.CharField("인증번호", max_length=30)

    class Meta:
        db_table = "authentications"
        verbose_name_plural = "휴대폰인증 관리 페이지"

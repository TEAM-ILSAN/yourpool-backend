from django.db import models

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
# Generated by Django 4.0.4 on 2022-09-24 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_yourpooluser_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yourpooluser',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='F', max_length=2),
        ),
    ]

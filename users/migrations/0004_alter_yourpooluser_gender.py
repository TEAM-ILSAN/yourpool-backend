# Generated by Django 4.0.4 on 2022-09-24 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_yourpooluser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yourpooluser',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='F', max_length=50),
        ),
    ]

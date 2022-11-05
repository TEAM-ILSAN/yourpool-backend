# Generated by Django 4.0.4 on 2022-11-05 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat_log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.IntegerField()),
                ('meet_time', models.DateTimeField()),
                ('chat_member', models.JSONField(null=True)),
                ('room_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'chat_log',
            },
        ),
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('room_id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(default='', max_length=50)),
                ('area', models.CharField(default='', max_length=50)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=1000, null=True)),
                ('lon', models.DecimalField(decimal_places=6, max_digits=1000, null=True)),
                ('room_category', models.CharField(choices=[('COFFEECHAT', '커피챗'), ('SPORT', '운동'), ('WALK', '산책'), ('ANIMAL', '반려동물'), ('HOBBY', '취미모임'), ('GAME', '게임'), ('STUDY', '스터디'), ('DRINK', '술자리'), ('FINANCIAL', '재테크'), ('CAREER', '커리어'), ('INFO', '동네정보'), ('FOOD', '밥친구')], max_length=15)),
                ('room_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('limit', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)], null=True)),
                ('status', models.IntegerField(choices=[('0', 'off'), ('1', 'on'), ('2', 'start')])),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('meet_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('chat_member', models.JSONField(null=True)),
            ],
            options={
                'db_table': 'chat_rooms',
            },
        ),
    ]

# Generated by Django 4.0.4 on 2022-09-17 14:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='target_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='report_targer_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='report',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='report_user', to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 4.0.4 on 2022-12-03 07:03

from django.db import migrations, models
import users.manage


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_yourpooluser_first_name_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='yourpooluser',
            managers=[
                ('objects', users.manage.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='yourpooluser',
            name='is_verified',
        ),
        migrations.AddField(
            model_name='yourpooluser',
            name='otp',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='yourpooluser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='yourpooluser',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
    ]

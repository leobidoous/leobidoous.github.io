# Generated by Django 2.2.9 on 2020-01-27 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_usermodel_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Team'),
        ),
    ]
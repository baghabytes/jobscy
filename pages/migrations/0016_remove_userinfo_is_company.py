# Generated by Django 4.2 on 2023-06-23 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_userinfo_is_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='is_company',
        ),
    ]
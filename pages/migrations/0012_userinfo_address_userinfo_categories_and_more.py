# Generated by Django 4.2.1 on 2023-06-21 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_userinfo_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='categories',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='education_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='experience_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='experience_years',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='qualification',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='salary',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='skype',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='cv_file',
            field=models.FileField(blank=True, null=True, upload_to='static/cv'),
        ),
    ]
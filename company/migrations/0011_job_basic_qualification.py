# Generated by Django 4.2.1 on 2023-06-26 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_job_experience_req_job_responsibilities_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='basic_qualification',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
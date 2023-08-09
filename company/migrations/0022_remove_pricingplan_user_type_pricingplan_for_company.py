# Generated by Django 4.2.1 on 2023-07-08 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0021_pricingplan_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricingplan',
            name='user_type',
        ),
        migrations.AddField(
            model_name='pricingplan',
            name='for_company',
            field=models.BooleanField(null=True),
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-28 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0014_job_is_approved'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.companyinfo')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.pricingplan')),
            ],
        ),
    ]
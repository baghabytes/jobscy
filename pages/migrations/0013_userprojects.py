# Generated by Django 4.2 on 2023-06-23 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_userinfo_address_userinfo_categories_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_file', models.FileField(blank=True, null=True, upload_to='static/candidate_project')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.userinfo')),
            ],
        ),
    ]

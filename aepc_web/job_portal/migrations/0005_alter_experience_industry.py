# Generated by Django 5.1.5 on 2025-01-22 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0004_experience_industry_alter_candidate_consultant_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='industry',
            field=models.CharField(max_length=255),
        ),
    ]

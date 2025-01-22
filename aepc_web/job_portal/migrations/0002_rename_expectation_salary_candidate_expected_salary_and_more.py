# Generated by Django 5.1.5 on 2025-01-21 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='expectation_salary',
            new_name='expected_salary',
        ),
        migrations.AlterField(
            model_name='candidate',
            name='designation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='linkedin_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

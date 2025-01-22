# Generated by Django 5.1.5 on 2025-01-20 07:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('linkedin_url', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('designation', models.CharField(max_length=255)),
                ('degree', models.CharField(max_length=100)),
                ('major', models.CharField(max_length=100)),
                ('gpa', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('college_name', models.CharField(max_length=255)),
                ('consultant_name', models.CharField(blank=True, max_length=100, null=True)),
                ('curr_salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('expectation_salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('cv', models.FileField(upload_to='uploaded_resumes/')),
                ('skills', models.TextField()),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField()),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='job_portal.candidate')),
            ],
        ),
    ]

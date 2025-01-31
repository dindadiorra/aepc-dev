from django.contrib import admin
from .models import Candidate, Experience, Job, JobApplication

admin.site.register(Candidate)
admin.site.register(Experience)
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'seniority_level', 'industry', 'created_at')
    search_fields = ('title', 'location', 'industry')
    list_filter = ('industry', 'seniority_level')
    ordering = ('-created_at',)
@admin.register(JobApplication)
class JobAppAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'job', 'applied_at')
    search_fields = ('candidate__full_name', 'job__title')
    list_filter = ('job', 'candidate')

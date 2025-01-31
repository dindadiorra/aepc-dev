from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField()
    designation = models.CharField(max_length=255, null=True, blank=True)
    degree = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    college_name = models.CharField(max_length=255)
    consultant_name = models.CharField(max_length=255, null=True, blank=True)
    curr_salary = models.IntegerField(null=True, blank=True)
    expected_salary = models.IntegerField(null=True, blank=True)
    cv = models.FileField(upload_to='uploaded_resumes/')
    skills = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Experience(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='experiences')
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    year = models.IntegerField(null=True, blank=True, default=None)
    month = models.IntegerField(null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.position} at {self.company_name}"

class Job(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    seniority_level = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    sub_industry = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    requirement_details = models.TextField()
    recruiter_email = models.CharField(max_length=255)
    recruiter_phone = models.CharField(max_length=15)
    job_poster = models.ImageField(upload_to='job_poster/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class JobApplication(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='applications')
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True, blank=True, related_name='applications')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidate.name} - {self.job.title if self.job else 'General Application'}"
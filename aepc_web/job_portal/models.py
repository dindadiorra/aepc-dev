from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)  # Optional
    address = models.TextField()
    designation = models.CharField(max_length=255, null=True, blank=True)  # Optional, internal use
    degree = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    college_name = models.CharField(max_length=255)
    consultant_name = models.CharField(max_length=100, null=True, blank=True)  # Optional, internal use
    curr_salary = models.IntegerField(null=True, blank=True)  # Optional
    expected_salary = models.IntegerField(null=True, blank=True)  # Optional
    cv = models.FileField(upload_to='uploaded_resumes/')  # Required
    skills = models.TextField()  # Required
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Experience(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='experiences')
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.position} at {self.company_name}"

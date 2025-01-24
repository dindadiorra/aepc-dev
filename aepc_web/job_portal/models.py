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
    # year = models.IntegerField(null=True, blank=True)
    # month = models.IntegerField(null=True, blank=True)

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


'''
1. Fitur Job List:
- Purpose: menampilkan daftar lowongan kerja
- Menggunakan cards dengan grid 3x3
- Untuk masing-masing card info yang ditampilkan: gambar di samping kiri (preview poster lowongan), job title, location, seniority level, industry & sub-industry, date posted, tombol view more.
- Pakai pagination dan loading menggunakan AJAX
- Menggunakan bootstrap
- Ada fungsionalitas Filter, Search, Sort (sebaris, sticky on top) (nanti)

1. Filter Job List
- Filter by Location: data kota, tapi bisa search location and filter berdasarkan itu
- Filter by Seniority Level: Internship, Entry Level/Junior/Apprentice, Associate/Supervisor, Mid-Senior Level/Manager, Director/Executive. (tolong improve lagi apa aja filternya)
- Filter by Industry: 
- Pakai Dropdown
- Pakai AJAX
- Pakai Bootstrap

2. Search Job List
- Search by apa?
- Pakai AJAX
- Pakai Bootstrap

3. Sort Job List
- Sort by date posted
- Pakai AJAX
- Pakai Bootstrap


'''
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Candidate, Experience, Job, JobApplication
from .forms import CandidateForm, ExperienceForm
import json
from django.core.paginator import Paginator

def home(request):
    return render(request, 'home.html')

def apply_or_upload_resume(request, job_id=None):
    job = get_object_or_404(Job, id=job_id) if job_id else None
    if request.method == 'POST':
        candidate_form = CandidateForm(request.POST, request.FILES)
        if candidate_form.is_valid():
            candidate = candidate_form.save(commit=False)
            
            degree = request.POST.get('degree')
            other_degree = request.POST.get('other_degree')
            candidate.degree = other_degree if degree == "Other" else degree

            candidate.save()

            if job:
                JobApplication.objects.create(candidate=candidate, job=job)

            try:              
                experiences_data = json.loads(request.POST.get('experiences', '[]'))
                for experience_data in experiences_data:
                    if experience_data.get('companyName') and experience_data.get('position') and experience_data.get('startDate'):
                        Experience.objects.create(
                            candidate=candidate,
                            company_name=experience_data.get('companyName'),
                            position=experience_data.get('position'),
                            industry=experience_data.get('industry'),
                            start_date=experience_data.get('startDate'),
                            end_date=experience_data.get('endDate', ''),
                            description=experience_data.get('description', '')
                        )

                return JsonResponse({
                    'success': True,
                    'message': 'Job Application saved successfully!' if job else 'Resume uploaded successfully!',
                    'candidate_id': candidate.id
                })
            except Exception as e:
                return JsonResponse({'success': False, 'errors': str(e)}, status=400)
        else:
            errors = candidate_form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        candidate_form = CandidateForm()

    return render(request, 'upload_resume.html', {'candidate_form': candidate_form, 'job': job})

def add_experience(request, candidate_id):
    candidate = get_object_or_404(Candidate, id=candidate_id)

    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.candidate = candidate
            experience.save()
            return JsonResponse({'success': True, 'message': 'Experience added successfully!'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)

    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})

def job_list_data(request):
    search_query = request.GET.get('search', '')
    filter_industry = request.GET.get('filter', '')
    sort_by = request.GET.get('sort', '-created_at')
    page = request.GET.get('page', 1)

    jobs = Job.objects.all()

    if search_query:
        jobs = jobs.filter(title__icontains=search_query)
    if filter_industry:
        jobs = jobs.filter(industry=filter_industry)

    jobs = jobs.order_by(sort_by)
    paginator = Paginator(jobs, 9)

    try:
        jobs_page = paginator.page(page)
    except Exception:
        jobs_page = []

    job_data = [
        {
            "id": job.id,
            "title": job.title,
            "location": job.location,
            "seniority_level": job.seniority_level,
            "industry": job.industry,
            "sub_industry": job.sub_industry,
            "created_at": job.created_at.strftime('%Y-%m-%d'),
            "job_poster": job.job_poster.url if job.job_poster else '/static/default-job.png',
        }
        for job in jobs_page
    ]

    return JsonResponse({
        "jobs": job_data,
        "has_next": jobs_page.has_next(),
    })

def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    return render(request, 'job_details.html', {
        'job': job
    })
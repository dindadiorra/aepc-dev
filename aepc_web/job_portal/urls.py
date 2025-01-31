from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('upload-resume/', views.apply_or_upload_resume, name='upload_resume'),
    path('add-experience/<int:candidate_id>/', views.add_experience, name='add_experience'),
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/data/', views.job_list_data, name='job_list_data'),
    path('jobs/<int:job_id>/', views.job_detail, name='job_detail'),
    path('apply/<int:job_id>/', views.apply_or_upload_resume, name='apply'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
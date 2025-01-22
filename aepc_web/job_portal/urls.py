from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload-resume/', views.upload_cv, name='upload_resume'),
    path('add-experience/<int:candidate_id>/', views.add_experience_ajax, name='add_experience_ajax'),
]

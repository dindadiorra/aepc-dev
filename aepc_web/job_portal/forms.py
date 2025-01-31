from django import forms
from .models import Candidate, Experience
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.core.validators import validate_email
import os

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = [
            'name', 'email', 'phone_number', 'linkedin_url', 'address', 'degree',
            'major', 'gpa', 'college_name', 'curr_salary', 'expected_salary', 'cv', 'skills'
        ]
        widgets = {
            'linkedin_url': forms.TextInput(attrs={'placeholder': 'LinkedIn Profile (Optional)'}),
            'curr_salary': forms.NumberInput(attrs={'placeholder': 'Current Salary (Optional)'}),
            'expected_salary': forms.NumberInput(attrs={'placeholder': 'Expected Salary (Optional)'}),
        }
        labels = {
            'cv': 'Upload CV (PDF/Word)',
        }
        
    def clean_cv(self):
        cv = self.cleaned_data.get('cv')
        if not cv:
            raise forms.ValidationError("CV is required.")
        if not cv.name.endswith('.pdf'):
            raise forms.ValidationError("CV must be a PDF file.")
        if cv.size > 10 * 1024 * 1024:
            raise forms.ValidationError("CV file size must be under 10MB.")
        return cv

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email is required.")
        try:
            validate_email(email)
        except ValidationError:
            raise forms.ValidationError("Enter a valid email address.")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number:
            raise forms.ValidationError("Phone number is required.")
        if not phone_number.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")
        return phone_number

    def clean_gpa(self):
        gpa = self.cleaned_data.get('gpa')
        if not gpa:
            raise forms.ValidationError("GPA is required.")
        try:
            gpa = float(gpa)
            if gpa < 0 or gpa > 4.00:
                raise forms.ValidationError("GPA must be between 0.00 and 4.00.")
        except ValueError:
            raise forms.ValidationError("GPA must be a number in the format 4.00.")
        return gpa

    def clean(self):
        cleaned_data = super().clean()
        required_fields = ['name', 'address', 'degree', 'major', 'college_name', 'skills']
        for field in required_fields:
            if not cleaned_data.get(field):
                self.add_error(field, f"{field.replace('_', ' ').capitalize()} is required.")
        return cleaned_data

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['company_name', 'position', 'industry', 'start_date', 'end_date', 'description']
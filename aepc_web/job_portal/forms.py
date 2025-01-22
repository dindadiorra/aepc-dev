from django import forms
from .models import Candidate, Experience
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

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
    
    def clean_curr_salary(self):
        curr_salary = self.cleaned_data.get('curr_salary')
        if curr_salary is not None and curr_salary < 0:
            raise forms.ValidationError("Current salary cannot be negative.")
        return curr_salary

    def clean_expected_salary(self):
        expected_salary = self.cleaned_data.get('expected_salary')
        if expected_salary is not None and expected_salary < 0:
            raise forms.ValidationError("Expected salary cannot be negative.")
        return expected_salary

    def clean_gpa(self):
        gpa = self.cleaned_data.get('gpa')
        if gpa is not None and gpa < 0:
            raise forms.ValidationError("GPA cannot be negative.")
        return gpa

    def clean_linkedin_url(self):
        linkedin_url = self.cleaned_data.get('linkedin_url')
        if linkedin_url:
            validator = URLValidator()
            try:
                if not linkedin_url.startswith(('http://', 'https://')):
                    linkedin_url = f"http://{linkedin_url}"
                validator(linkedin_url)
            except ValidationError:
                raise forms.ValidationError("Invalid LinkedIn URL. Please ensure the format is correct.")
        return linkedin_url



class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['company_name', 'position', 'start_date', 'end_date', 'description']
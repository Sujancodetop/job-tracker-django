from django import forms
from .models import JobApplication
class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['company_name', 'position', 'date_applied', 'status']
        widgets = {
            'date_applied': forms.DateInput(attrs={'type': 'date'}),
        }

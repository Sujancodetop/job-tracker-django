from django.contrib import admin
from .models import JobApplication

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'position', 'date_applied', 'status')
    

# Register your models here.admin.site.register
(JobApplication,JobApplicationAdmin)

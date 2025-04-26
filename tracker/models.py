from django.db import models
class JobApplication(models.Model):
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    date_applied = models.DateField()
    status=models.CharField(max_length=100,choices=[
    ('Applied','Applied'),
    ('Interview','Interview'),
    ('Offer','Offer'),
    ('Rejected','Rejected'),
])
notes = models.TextField(blank=True, null=True)
def __str__(self):
    return f"{self.company_name} - {self.job_title}"

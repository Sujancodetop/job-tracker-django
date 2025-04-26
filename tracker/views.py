from django.shortcuts import get_object_or_404 
from django.shortcuts import render
from .models import JobApplication
def home(request):
   jobs=JobApplication.objects.all()
   return render(request,'tracker/home.html',{'jobs':jobs})
# Create your views here.
from .forms import JobApplicationForm
from django.shortcuts import redirect
def add_job(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JobApplicationForm()
    return render(request, 'tracker/add_job.html', {'form': form})
def edit_job(request,job_id):





























































    job=get_object_or_404(JobApplication,id=job_id)
    if request.method=='POST':
        form=JobApplicationForm(request.POST,instance=job)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=JobApplicationForm(instance=job)
    return render(request,'tracker/edit_job.html',{'form':form,'job':job})
def delete_job(request,job_id):
    job=get_object_or_404(JobApplication,id=job_id)
    job.delete()
    return redirect('home')
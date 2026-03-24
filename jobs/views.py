from django.shortcuts import render
from .models import Job

def job_list(request):
    jobs = Job.objects.all().order_by('-created_at')
    return render(request, 'job_list.html', {'jobs': jobs})
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse
from .models import Job
from .filters import JobFilter
from .forms import JobForm
from comments.models import Comment
from comments.forms import CommentForm

def job_list(request):
    jobs = Job.objects.filter(is_active=True, expiry_date__gt=timezone.now())
    job_filter = JobFilter(request.GET, queryset=jobs)
    filtered_jobs = job_filter.qs
    
    paginator = Paginator(filtered_jobs, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'filter': job_filter,
        'total_jobs': filtered_jobs.count(),
    }
    
    if request.htmx:
        return render(request, 'jobs/partials/job_list.html', context)
    
    return render(request, 'jobs/job_list.html', context)

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk, is_active=True)
    comments = Comment.objects.filter(job=job, is_approved=True).order_by('-posted_date')
    comment_form = CommentForm()
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.job = job
            comment.save()
            messages.success(request, 'Your comment has been submitted and is awaiting approval.')
            return redirect('job_detail', pk=job.pk)
    
    context = {
        'job': job,
        'comments': comments,
        'comment_form': comment_form,
    }
    
    return render(request, 'jobs/job_detail.html', context)

def job_create(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            # Set created_by if user is authenticated, otherwise leave it None
            if request.user.is_authenticated:
                job.created_by = request.user
            job.save()
            form.save_m2m()  # Save translations
            messages.success(request, 'Your job has been posted successfully!')
            return redirect('job_detail', pk=job.pk)
    else:
        form = JobForm()
    
    return render(request, 'jobs/job_create.html', {'form': form})

import django_filters
from django import forms
from .models import Job

class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={
            'placeholder': 'Search jobs...',
            'class': 'w-full px-4 py-2 border border-gray-200 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent'
        })
    )
    
    job_type = django_filters.ChoiceFilter(
        choices=Job.JOB_TYPE_CHOICES,
        empty_label="All Job Types",
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-2 border border-gray-200 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent'
        })
    )
    
    location_type = django_filters.ChoiceFilter(
        choices=Job.LOCATION_TYPE_CHOICES,
        empty_label="All Locations",
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-2 border border-gray-200 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent'
        })
    )
    
    class Meta:
        model = Job
        fields = ['title', 'job_type', 'location_type']

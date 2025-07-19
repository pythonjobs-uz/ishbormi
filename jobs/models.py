from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from parler.models import TranslatableModel, TranslatedFields
from django.urls import reverse

class Job(TranslatableModel):
    JOB_TYPE_CHOICES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('freelance', 'Freelance'),
    ]
    
    LOCATION_TYPE_CHOICES = [
        ('remote', 'Remote'),
        ('online', 'Online'),
        ('offline', 'Offline'),
    ]
    
    company_name = models.CharField(max_length=255)
    company_logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    job_type = models.CharField(max_length=50, choices=JOB_TYPE_CHOICES)
    salary = models.CharField(max_length=100, blank=True)
    location_type = models.CharField(max_length=50, choices=LOCATION_TYPE_CHOICES)
    posted_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField()
    is_enhanced = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        description=models.TextField(),
    )
    
    class Meta:
        ordering = ['-is_enhanced', '-posted_date']
        indexes = [
            models.Index(fields=['job_type', 'location_type']),
            models.Index(fields=['posted_date']),
            models.Index(fields=['is_enhanced']),
        ]
    
    def save(self, *args, **kwargs):
        if not self.expiry_date:
            self.expiry_date = timezone.now() + timedelta(days=30)
        super().save(*args, **kwargs)
    
    def is_expired(self):
        return timezone.now() > self.expiry_date
    
    def get_absolute_url(self):
        return reverse('job_detail', kwargs={'pk': self.pk})
    
    def __str__(self):
        return f"{self.safe_translation_getter('title', any_language=True)} at {self.company_name}"

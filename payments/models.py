from django.db import models
from jobs.models import Job

class Payment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=22000.00)
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Payment for {self.job.title} - {self.status}"

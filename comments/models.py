from django.db import models
from jobs.models import Job

class Comment(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    text = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-posted_date']
    
    def __str__(self):
        return f"Comment by {self.name} on {self.job.title}"

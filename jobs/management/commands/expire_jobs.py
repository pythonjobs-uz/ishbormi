from django.core.management.base import BaseCommand
from django.utils import timezone
from jobs.models import Job

class Command(BaseCommand):
    help = 'Mark expired jobs as inactive'

    def handle(self, *args, **options):
        expired_jobs = Job.objects.filter(
            is_active=True,
            expiry_date__lt=timezone.now()
        )
        
        count = expired_jobs.count()
        expired_jobs.update(is_active=False)
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully expired {count} jobs')
        )

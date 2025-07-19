import os
import sys
import django
from datetime import datetime, timedelta

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ishbormi.settings')
django.setup()

from django.contrib.auth.models import User
from jobs.models import Job
from comments.models import Comment

def create_sample_data():
    print("Creating sample data for Ishbormi job board...")
    
    # Create a sample user
    user, created = User.objects.get_or_create(
        username='admin',
        defaults={
            'email': 'admin@ishbormi.uz',
            'is_staff': True,
            'is_superuser': True
        }
    )
    if created:
        user.set_password('admin123')
        user.save()
        print("✓ Created admin user: admin/admin123")
    else:
        print("✓ Admin user already exists")

    # Sample job data
    sample_jobs = [
        {
            'title': 'Senior Python Developer',
            'company_name': 'TechCorp Uzbekistan',
            'job_type': 'full_time',
            'location_type': 'remote',
            'salary': '8,000,000 - 12,000,000 UZS',
            'description': '''We are looking for an experienced Python developer to join our growing team.

Requirements:
- 3+ years of Python experience
- Django/Flask framework knowledge
- PostgreSQL database experience
- Git version control
- English proficiency

Responsibilities:
- Develop and maintain web applications
- Write clean, maintainable code
- Collaborate with cross-functional teams
- Participate in code reviews

Benefits:
- Competitive salary
- Remote work flexibility
- Professional development opportunities
- Health insurance''',
            'is_enhanced': True
        },
        {
            'title': 'Frontend Developer (React)',
            'company_name': 'Digital Solutions',
            'job_type': 'full_time',
            'location_type': 'offline',
            'salary': '6,000,000 - 9,000,000 UZS',
            'description': '''Join our frontend team to build amazing user interfaces.

Requirements:
- React.js experience
- JavaScript ES6+
- HTML5/CSS3
- Responsive design
- Git knowledge

What we offer:
- Modern office in Tashkent
- Flexible working hours
- Team building events
- Career growth opportunities''',
            'is_enhanced': False
        },
        {
            'title': 'UI/UX Designer',
            'company_name': 'Creative Agency',
            'job_type': 'part_time',
            'location_type': 'online',
            'salary': '4,000,000 - 6,000,000 UZS',
            'description': '''We need a creative UI/UX designer for our projects.

Skills required:
- Figma/Adobe XD
- User research
- Prototyping
- Visual design
- Portfolio required

This is a part-time position with flexible hours.''',
            'is_enhanced': False
        },
        {
            'title': 'DevOps Engineer',
            'company_name': 'CloudTech',
            'job_type': 'full_time',
            'location_type': 'remote',
            'salary': '10,000,000 - 15,000,000 UZS',
            'description': '''Looking for a DevOps engineer to manage our infrastructure.

Requirements:
- Docker/Kubernetes
- AWS/Azure experience
- CI/CD pipelines
- Linux administration
- Monitoring tools

Benefits:
- High salary
- Remote work
- Latest technology stack
- International projects''',
            'is_enhanced': True
        },
        {
            'title': 'Mobile App Developer',
            'company_name': 'MobileTech',
            'job_type': 'freelance',
            'location_type': 'remote',
            'salary': 'Project-based',
            'description': '''Freelance mobile app developer needed for iOS/Android projects.

Skills:
- React Native or Flutter
- Native development (iOS/Android)
- API integration
- App store deployment

This is a project-based freelance position.''',
            'is_enhanced': False
        }
    ]

    # Create sample jobs
    jobs_created = 0
    for job_data in sample_jobs:
        job, created = Job.objects.get_or_create(
            title=job_data['title'],
            company_name=job_data['company_name'],
            defaults={
                **job_data,
                'created_by': user,
                'expiry_date': datetime.now() + timedelta(days=30)
            }
        )
        if created:
            jobs_created += 1
            print(f"✓ Created job: {job.title}")

            # Add sample comments
            sample_comments = [
                {
                    'name': 'Akmal Karimov',
                    'text': 'Great opportunity! Is remote work available?',
                    'is_approved': True
                },
                {
                    'name': 'Dilnoza Rashidova',
                    'text': 'What are the working hours for this position?',
                    'is_approved': True
                }
            ]

            for comment_data in sample_comments:
                Comment.objects.create(
                    job=job,
                    **comment_data
                )
        else:
            print(f"✓ Job already exists: {job.title}")

    print(f"\n🎉 Sample data creation completed!")
    print(f"📊 Created {jobs_created} new jobs")
    print(f"👤 Admin credentials: admin / admin123")
    print(f"🌐 Access admin at: http://localhost:8000/admin/")

if __name__ == '__main__':
    create_sample_data()

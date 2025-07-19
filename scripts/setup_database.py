import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ishbormi.settings')
django.setup()

from django.core.management import execute_from_command_line

def setup_database():
    print("Setting up Ishbormi database...")
    
    # Make migrations
    print("Creating migrations...")
    execute_from_command_line(['manage.py', 'makemigrations'])
    
    # Apply migrations
    print("Applying migrations...")
    execute_from_command_line(['manage.py', 'migrate'])
    
    # Collect static files
    print("Collecting static files...")
    execute_from_command_line(['manage.py', 'collectstatic', '--noinput'])
    
    print("✅ Database setup completed!")
    print("Next steps:")
    print("1. Run: python scripts/create_sample_data.py")
    print("2. Start server: python manage.py runserver")

if __name__ == '__main__':
    setup_database()

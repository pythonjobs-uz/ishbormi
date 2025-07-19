# Ishbormi Job Board Setup Guide

## Prerequisites

- Python 3.11+
- PostgreSQL 15+
- Redis (optional, for caching)
- Git

## Quick Setup

### 1. Clone and Setup Environment

\`\`\`bash
git clone <repository-url>
cd ishbormi-job-board
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
\`\`\`

### 2. Database Setup

\`\`\`bash
# Create PostgreSQL database
createdb ishbormi_db

# Copy environment file
cp .env.example .env
# Edit .env with your database credentials

# Setup database
python scripts/setup_database.py
\`\`\`

### 3. Create Sample Data

\`\`\`bash
python scripts/create_sample_data.py
\`\`\`

### 4. Run Development Server

\`\`\`bash
python manage.py runserver
\`\`\`

Visit http://localhost:8000 to see the job board!

## Admin Access

- URL: http://localhost:8000/admin/
- Username: admin
- Password: admin123

## Docker Setup (Alternative)

\`\`\`bash
docker-compose up --build
\`\`\`

## Features Implemented

✅ **Core Features**
- Job listing with filtering and search
- Enhanced jobs with gradient backgrounds
- Comment system (no login required)
- Bilingual support (Uzbek/Russian)
- Payment integration structure
- Admin panel with Django Unfold

✅ **UI/UX**
- Minimalist white design
- Responsive layout
- Smooth animations
- HTMX for dynamic filtering

✅ **Backend**
- Django 5.x with PostgreSQL
- Optimized database queries
- Automatic job expiration
- Translation support

## Management Commands

\`\`\`bash
# Expire old jobs
python manage.py expire_jobs

# Create translations
python manage.py makemessages -l uz -l ru
python manage.py compilemessages
\`\`\`

## Production Deployment

1. Set DEBUG=False in settings
2. Configure proper SECRET_KEY
3. Set up PostgreSQL and Redis
4. Use Gunicorn + Nginx
5. Configure HTTPS
6. Set up automated backups

## API Integration

The Mirpay.uz integration is structured but needs actual API implementation based on their documentation.

## Support

For issues or questions, please check the documentation or create an issue in the repository.

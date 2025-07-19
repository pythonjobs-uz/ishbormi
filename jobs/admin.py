from django.contrib import admin
from unfold.admin import ModelAdmin
from parler.admin import TranslatableAdmin
from .models import Job

@admin.register(Job)
class JobAdmin(TranslatableAdmin, ModelAdmin):
    list_display = ['title', 'company_name', 'job_type', 'location_type', 'is_enhanced', 'posted_date', 'expiry_date', 'is_active']
    list_filter = ['job_type', 'location_type', 'is_enhanced', 'is_active', 'posted_date']
    search_fields = ['translations__title', 'company_name', 'translations__description']
    list_editable = ['is_enhanced', 'is_active']
    readonly_fields = ['posted_date']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'company_name', 'company_logo', 'description')
        }),
        ('Job Details', {
            'fields': ('job_type', 'location_type', 'salary')
        }),
        ('Status', {
            'fields': ('is_enhanced', 'is_active', 'posted_date', 'expiry_date')
        }),
        ('User', {
            'fields': ('created_by',)
        }),
    )
    
    def get_prepopulated_fields(self, request, obj=None):
        return {}

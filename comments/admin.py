from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ['name', 'get_job_title', 'posted_date', 'is_approved']
    list_filter = ['is_approved', 'posted_date']
    search_fields = ['name', 'text', 'job__translations__title']
    list_editable = ['is_approved']
    readonly_fields = ['posted_date']
    
    fieldsets = (
        ('Comment Details', {
            'fields': ('job', 'name', 'text', 'posted_date')
        }),
        ('Moderation', {
            'fields': ('is_approved',)
        }),
    )
    
    def get_job_title(self, obj):
        return obj.job.safe_translation_getter('title', any_language=True) or 'Untitled Job'
    get_job_title.short_description = 'Job'

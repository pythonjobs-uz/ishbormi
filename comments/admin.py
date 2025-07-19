from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ['name', 'job', 'posted_date', 'is_approved']
    list_filter = ['is_approved', 'posted_date']
    search_fields = ['name', 'text', 'job__title']
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

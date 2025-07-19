from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(ModelAdmin):
    list_display = ['job', 'amount', 'transaction_id', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['transaction_id', 'job__title']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Payment Details', {
            'fields': ('job', 'amount', 'transaction_id', 'status')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )

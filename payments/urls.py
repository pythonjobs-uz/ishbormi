from django.urls import path
from . import views

urlpatterns = [
    path('enhance/<int:job_id>/', views.enhance_job, name='enhance_job'),
    path('success/<int:payment_id>/', views.payment_success, name='payment_success'),
    path('cancel/<int:payment_id>/', views.payment_cancel, name='payment_cancel'),
    path('callback/', views.payment_callback, name='payment_callback'),
]

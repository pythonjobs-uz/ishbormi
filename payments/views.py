from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import requests
import json
import uuid
from .models import Payment
from jobs.models import Job

def enhance_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    
    if request.method == 'POST':
        # Create payment record
        payment = Payment.objects.create(
            job=job,
            transaction_id=str(uuid.uuid4()),
            amount=settings.ENHANCED_JOB_PRICE
        )
        
        # Redirect to Mirpay.uz
        mirpay_url = f"{settings.MIRPAY_BASE_URL}/payment"
        payment_data = {
            'store_name': settings.MIRPAY_STORE_NAME,
            'kassa_id': settings.MIRPAY_KASSA_ID,
            'api_key': settings.MIRPAY_API_KEY,
            'amount': float(payment.amount),
            'transaction_id': payment.transaction_id,
            'return_url': request.build_absolute_uri(f'/payments/success/{payment.id}/'),
            'cancel_url': request.build_absolute_uri(f'/payments/cancel/{payment.id}/'),
        }
        
        # In a real implementation, you would make an API call to Mirpay.uz
        # For now, we'll simulate the payment process
        return redirect('payment_success', payment_id=payment.id)
    
    return render(request, 'payments/enhance_job.html', {'job': job})

def payment_success(request, payment_id):
    payment = get_object_or_404(Payment, pk=payment_id)
    payment.status = 'completed'
    payment.save()
    
    # Enhance the job
    job = payment.job
    job.is_enhanced = True
    job.save()
    
    return render(request, 'payments/success.html', {'payment': payment})

def payment_cancel(request, payment_id):
    payment = get_object_or_404(Payment, pk=payment_id)
    payment.status = 'failed'
    payment.save()
    
    return render(request, 'payments/cancel.html', {'payment': payment})

@csrf_exempt
def payment_callback(request):
    # Handle Mirpay.uz callback
    if request.method == 'POST':
        data = json.loads(request.body)
        transaction_id = data.get('transaction_id')
        status = data.get('status')
        
        try:
            payment = Payment.objects.get(transaction_id=transaction_id)
            payment.status = 'completed' if status == 'success' else 'failed'
            payment.save()
            
            if payment.status == 'completed':
                job = payment.job
                job.is_enhanced = True
                job.save()
            
            return JsonResponse({'status': 'ok'})
        except Payment.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Payment not found'})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

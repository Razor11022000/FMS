from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
	return render(request, 'accounts/dashboard.html')

def student(request):
	return render(request, 'accounts/student.html')

def payment(request):
	payments = Payment.objects.all()

	return render(request, 'accounts/payment.html', {'payments':payments} )

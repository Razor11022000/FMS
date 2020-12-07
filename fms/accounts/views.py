from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import PaymentForm
# Create your views here.

def home(request):

	students = Student.objects.all()
	payments = Payment.objects.all()

	Total_payments = payments.count()
	Payments_recieved = payments.filter(status='Recieved').count()
	Payments_pending = payments.filter(status='Pending').count()

	context = {'students':students, 'payments':payments, 'Total_payments':Total_payments,
	'Payments_recieved':Payments_recieved, 'Payments_pending':Payments_pending}

	return render(request, 'accounts/dashboard.html',context)


def student(request, pk):
	student = Student.objects.get(id=pk)
	payments= student.payment_set.all()

	payment_count = payments.filter(status='Pending').count()

	context = {'student':student, 'payments':payments, 'payment_count':payment_count}

	return render(request, 'accounts/student.html', context)


def payment(request):
	payments = Payment.objects.all()

	return render(request, 'accounts/payment.html', {'payments':payments} )


def createPayment(request):

	form = PaymentForm()

	if (request.method == 'POST'):
		form = PaymentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/payment_form.html', context)


def updatePayment(request, pk):

	payment = Payment.objects.get(id=pk)
	form = PaymentForm(instance=payment)

	if (request.method == 'POST'):
		form = PaymentForm(request.POST, instance=payment)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}

	return render(request, 'accounts/payment_form.html', context)


def deletePayment(request, pk):

	payment = Payment.objects.get(id=pk)

	if (request.method == 'POST'):
		payment.delete()
		return redirect('/')

	context = {'item':payment}
	return render(request, 'accounts/delete.html', context)

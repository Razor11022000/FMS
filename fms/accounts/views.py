from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import PaymentForm, CreateUserForm, UpdateStudentForm, ProfileForm, TcForm
from .filters import PaymentFilter
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.
@unauthenticated_user
def Register(request):

	form = CreateUserForm()
	if request.method == "POST":
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')


			messages.success(request, 'Account created ' + username)

			return redirect('login')

	context = {'form':form}
	return render(request,'accounts/register.html', context)


@unauthenticated_user
def Login(request):

	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')

		else:
			message.info(request, "Username or Password is Incorrect")

	context = {}
	return render(request, 'accounts/login.html', context)


def LogOut(request):

	logout(request)
	return redirect('login')


#--------- view function which renders USER.HTML page ---------#
@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def userPage(request):

	payments = request.user.student.payment_set.all()
	Total_payments = payments.count()
	Payments_recieved = payments.filter(status='Recieved').count()
	Payments_pending = payments.filter(status='Pending').count()

	context = {'payments':payments,'Total_payments':Total_payments, 'Payments_recieved':Payments_recieved,
	'Payments_pending':Payments_pending}
	return render(request, 'accounts/user.html', context)


#--------- view function which renders DASHBOARD.HTML page ----------#
@login_required(login_url='login')
@admin_only
def home(request):

	students = Student.objects.all()
	payments = Payment.objects.all()

	Total_payments = payments.count()
	Payments_recieved = payments.filter(status='Recieved').count()
	Payments_pending = payments.filter(status='Pending').count()

	context = {'students':students, 'payments':payments, 'Total_payments':Total_payments,
	'Payments_recieved':Payments_recieved, 'Payments_pending':Payments_pending}

	return render(request, 'accounts/newDashboard.html',context)


#--------- view function to render STUDENT.HTML page ----------#
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def student(request, pk):
	student = Student.objects.get(id=pk)
	payments= student.payment_set.all()

	payment_count = payments.filter(status='Pending').count()


	context = {'student':student, 'payments':payments, 'payment_count':payment_count}

	return render(request, 'accounts/student_info.html', context)


#--------- view function to render PROFILE_PAGE.HTML ----------#
@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def profileSettings(request):
	student = request.user.student
	form = ProfileForm(instance=student)
	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES, instance=student)
		if form.is_valid():
			form.save()

	context = {'form':form, 'student':student}
	return render(request, 'accounts/profile_page.html', context)


#--------- view fuction to render PAYMENT.HTML page ----------#
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def payment(request):
	#students = Student.objects.all()
	payments = Payment.objects.all()
	
	#payment = students.payment_set.all()

	#myFilter = PaymentFilter(request.GET, queryset=payment)
	#payment = myFilter.qs

	context = {'payments':payments}
	return render(request, 'accounts/payment.html', context)


#--------- view fuction which creates new payment ----------#
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def addPayment(request):

	form = PaymentForm()
	if request.method == "POST":
		form = PaymentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/payment_form.html', context)


#--------- view fuction which adds payment for a particular student ----------#
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createPayment(request, pk):

	student = Student.objects.get(id=pk)
	form = PaymentForm(initial={'student':student})

	if (request.method == 'POST'):
		form = PaymentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/payment_form.html', context)


#--------- view function which renders PAYMENT_FORM.HTML page ----------#
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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


#--------- view function which renders DELETE.HTML page ----------#
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deletePayment(request, pk):

	payment = Payment.objects.get(id=pk)

	if request.method == 'POST':
		payment.delete()
		return redirect('/')

	context = {'item':payment}
	return render(request, 'accounts/delete.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateStudent(request, pk):

	student = Student.objects.get(id=pk)
	form = UpdateStudentForm(instance=student)

	if request.method == "POST":
		form = UpdateStudentForm(request.POST, instance=student)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/updatestudent_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createTc(request, pk):

	tc = Tc.objects.get(student_id=pk)

	context = {'student':student,'tc':tc}
	return render(request, 'accounts/sample_tc.html', context)

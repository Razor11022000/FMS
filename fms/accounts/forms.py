from django.forms import ModelForm
from .models import Payment, Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class ProfileForm(ModelForm):
	class Meta:
		model = Student
		fields = ['name','phone','email','profile_pic']
		exclude = ['user']

class PaymentForm(ModelForm):
	class Meta:
		model = Payment
		fields =  '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class UpdateStudentForm(ModelForm):
	class Meta:
		model = Student
		fields = ['name','usn','phone','email','father_name','dob','nationality','gender','ad_date','batch','branch','profile_pic','category','attendence','cgpa']

class TcForm(ModelForm):
	class Meta:
		model = Student
		fields = '__all__'


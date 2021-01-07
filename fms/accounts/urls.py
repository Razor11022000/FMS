from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name = 'home'),
	path('register/',views.Register, name = 'register'),
	path('login/',views.Login, name = 'login'),
	path('logout/',views.LogOut, name = 'logout'),

	path('user/',views.userPage, name = 'userPage'),
    path('profile/',views.profileSettings, name = 'profile'),

    path('student/<str:pk>/', views.student, name = 'student'),    
    path('update_student/<str:pk>/', views.updateStudent, name = 'update_student'),
    path('payment/', views.payment, name = 'payment'),
    path('add_payment/', views.addPayment, name = 'add_payment'),

    path('create_payment/<str:pk>/', views.createPayment, name = 'create_payment'),
    path('update_payment/<str:pk>/', views.updatePayment, name = 'update_payment'),
    path('delete_payment/<str:pk>/', views.deletePayment, name = 'delete_payment'),

    path('tc-form/',views.tc, name = 'tc'),
    path('newDashboard/',views.newDashboard, name = 'newDashboard'),
]

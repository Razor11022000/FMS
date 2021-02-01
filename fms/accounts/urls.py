from django.urls import path
from django.contrib.auth import views as auth_views
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


    path('tc-form/<str:pk>/',views.createTc, name = 'create_tc'),
    path('newDashboard/',views.home, name = 'newDashboard'),
    path('chart/',views.chart),

    path('about/',views.aboutPage, name = 'about'),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), 
        name="password_reset_complete"),
]

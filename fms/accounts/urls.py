from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('student/<str:pk>/', views.student, name = 'student'),
    path('payment/', views.payment, name = 'payment'),

    path('create_payment/', views.createPayment, name = 'create_payment'),
    path('update_payment/<str:pk>/', views.updatePayment, name = 'update_payment'),
    path('delete_payment/<str:pk>/', views.deletePayment, name = 'delete_payment'),
]

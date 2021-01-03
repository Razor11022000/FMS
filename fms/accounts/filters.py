import django_filters

from .models import *

class PaymentFilter(django_filters.FilterSet):
	class Meta:
		model = Payment
		fields = '__all__'
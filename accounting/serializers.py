from rest_framework import serializers
from .models import *

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields= '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields ='__all__'
         
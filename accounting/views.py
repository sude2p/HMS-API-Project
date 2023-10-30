from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from core.permissions import CustomModelPermission
from rest_framework.generics import GenericAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.

#---------------- View for Bill Model----------------------------------------------#

class BillSerializerView(GenericAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes =[CustomModelPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields =['guest']

    def get(self, request):
        queryset = self.get_queryset()
        filter_queryset = self.filter_queryset(queryset)
        serializer = self.serializer_class(filter_queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('data created')
        else:
            return Response(serializer.errors)
        

class BillSerializerIdApiView(GenericAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [CustomModelPermission]

    def get(self, request, pk):
        try:
            queryset = Bill.objects.get(id=pk)
        except:
            return Response('Data Not Found')
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)

    def put(self, request, pk):
        queryset = Bill.objects.get(id=pk) 
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Data Updated')
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        queryset = Bill.objects.get(id=pk)
        queryset.delete()
        return Response('data deleted')
    
#-----------------------------------------------------------------------------------------------#

#---------------- View for Payment Model----------------------------------------------#

class PaymentSerializerView(GenericAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes =[CustomModelPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields =['bill']

    def get(self, request):
        queryset = self.get_queryset()
        filter_queryset = self.filter_queryset(queryset)
        serializer = self.serializer_class(filter_queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('data created')
        else:
            return Response(serializer.errors)
        

class PaymentSerializerIdApiView(GenericAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [CustomModelPermission]

    def get(self, request, pk):
        try:
            queryset = Payment.objects.get(id=pk)
        except:
            return Response('Data Not Found')
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)

    def put(self, request, pk):
        queryset = Payment.objects.get(id=pk) 
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Data Updated')
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        queryset = Payment.objects.get(id=pk)
        queryset.delete()
        return Response('data deleted')
#-----------------------------------------------------------------------------------------------#    
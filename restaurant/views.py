from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from core.permissions import CustomModelPermission
from rest_framework.generics import GenericAPIView
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# Create your views here.

#---------------- View for Menu Model-----------------------------------------------------#

class MenuSerializerApiView(GenericAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [CustomModelPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']
    #filterset_fields =[]

    def get(self, request):
        queryset = self.get_queryset()
        filter_queryset = self.filter_queryset(queryset)
        serializer = self.serializer_class(filter_queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Data Created')
        else:
            return Response(serializer.errors)

class MenuSerializerIdApiView(GenericAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [CustomModelPermission]

    def get(self, request, pk):
        try:
            queryset = Menu.objects.get(id=pk)
        except:
            return Response('data not found')
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)
        
    def put(self, request, pk):
        queryset = Menu.objects.get(id=pk)
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('data updated')
        
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        queryset = Menu.objects.get(id=pk)
        queryset.delete()
        return Response('data deleted!')   
    #---------------- --------------------------------------------------------------------#   

    #---------------- View for Food Model-----------------------------------------------------#

class FoodSerializerApiView(GenericAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [CustomModelPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']
    filterset_fields =['menu']

    def get(self, request):
        queryset = self.get_queryset()
        filter_queryset = self.filter_queryset(queryset)
        serializer = self.serializer_class(filter_queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Data Created')
        else:
            return Response(serializer.errors)

class FoodSerializerIdApiView(GenericAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [CustomModelPermission]

    def get(self, request, pk):
        try:
            queryset = Food.objects.get(id=pk)
        except:
            return Response('data not found')
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)
        
    def put(self, request, pk):
        queryset = Food.objects.get(id=pk)
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('data updated')
        
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        queryset = Food.objects.get(id=pk)
        queryset.delete()
        return Response('data deleted!')   

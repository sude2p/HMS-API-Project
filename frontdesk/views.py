from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from core.permissions import CustomModelPermission
from django.contrib.auth.models import Group
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.
# #function based view
# @api_view(['GET']) 
# def guestInfoApiView(request):
#     queryset = GuestInfo.objects.all()
#     serializer = GuestInfoSerializer(queryset, many=True)
#     return Response(serializer.data)

#class based view

#---------------- View for GuestInfo Model-----------------------------------------------------#

class GuestInfoApiView(GenericAPIView):
    queryset = GuestInfo.objects.all()       
    serializer_class = GuestInfoSerializer 
    permission_classes = [CustomModelPermission] 
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['f_name', 'l_name']  
    filterset_fields = ['f_name', 'l_name']                                          

    def get(self, request):
        queryset = self.get_queryset()        #----get_queryset method hits GuestInfo.objects.all() method
        # serializer = self.serializer_class(queryset, many=True)  define like this if no need for filter and search
        filter_queryset = self.filter_queryset(queryset)
        serializer = self.serializer_class(filter_queryset, many=True)
        return Response(serializer.data) 

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Data Created!!')
        else:
            return Response(serializer.errors)

class GuestInfoIdApiView(GenericAPIView):
    queryset = GuestInfo.objects.all()
    serializer_class = GuestInfoSerializer
    permission_classes = [CustomModelPermission]

    def get(self, request, pk):
        try:
            queryset = GuestInfo.objects.get(id=pk)
        except:
            return Response('Data not found')     
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)
    
    def put(self, request, pk):
        queryset = GuestInfo.objects.get(id=pk)
        serializer = self.serializer_class(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Data Updated')
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        queryset = GuestInfo.objects.get(id=pk)
        queryset.delete()
        return Response('data deleted!') 
#---------------- --------------------------------------------------------------------#    

#---------------- View for RoomType Model----------------------------------------------#

class RoomTypeApiView(GenericAPIView):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer
    permission_classes = [CustomModelPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']
    # filterset_fields = ['name']

    def get(self, request):           # get all  room type info
        queryset = self.get_queryset()
        filter_queryset = self.filter_queryset(queryset)
        serializer = self.serializer_class(filter_queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):              #create a roomtype 
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('RoomType data saved')
        else:
            return Response(serializer.errors)
        
    
    
class RoomTypeIdApiVieww(GenericAPIView):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer
    permission_classes =[CustomModelPermission]

    def get(self, request, pk): #function to get spicific roomtype
        try:
            queryset = RoomType.objects.get(id=pk)
        except:
            return Response('Data not found')    

        serializer = self.serializer_class(queryset)
        return Response(serializer.data)
    
    def put(self, request, pk):  #function to modify/update specific roomtype as id
        queryset = RoomType.objects.get(id=pk)
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('RoomType modified')
        else:
            return Response(serializer.errors)
        

    def delete(self, request, pk): # function  to delete specific roomtype
        queryset = RoomType.objects.get(id=pk)
        queryset.delete()
        return Response('RoomType deleted')

#---------------- -------------------------------------------------------------------------#


#---------------- View for Room Model----------------------------------------------#

class RoomApiView(GenericAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [CustomModelPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['status','floor']
    filterset_fields = ['room_type']

    def get(self, request):
        queryset = self.get_queryset()
        filter_queryset = self.filter_queryset(queryset)
        serializer = self.serializer_class(filter_queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class RoomApiIdView(GenericAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [CustomModelPermission]

    def get(self, request, pk):
        try:
            queryset = Room.objects.get(id=pk)

        except:
            return Response('Data not found')
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)

    def put(self, request, pk):
        queryset = Room.objects.get(id=pk)
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Room data Updataed')
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        queryset = Room.objects.get(id=pk)
        queryset.delete()
        return Response('Data deleted')

#-----------------------------------------------------------------------------------#

#---------------- View for GuestRoom Model----------------------------------------------#

class GuestRoomApiView(GenericAPIView):
    queryset = GuestRoom.objects.all()
    serializer_class = GuestRoomSerializer
    permission_classes = [CustomModelPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # search_fields = []
    filterset_fields = ['guest','room_no']

    def get(self, request):
        queryset = self.get_object()
        filter_queryset = self.filter_queryset(queryset)
        serializer = self.serializer_class(filter_queryset, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('data saved')
        else:
            return Response(serializer.errors)

class GuestRoomApiIdView(GenericAPIView):
    queryset = GuestRoom.objects.all()
    serializer_class = GuestRoomSerializer
    permission_classes = [CustomModelPermission]

    def get(self, request, pk):
        try:
            queryset = GuestRoom.objects.get(id=pk)
        except:
            return Response('Data Not Found')    
        serializer = self.serializer_class(queryset)
        return Response(serializer)
    
    def put(self, request, pk):
        queryset = GuestRoom.objects.get(id=pk)
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('GuestRoom data updated')
        else:
            return Response(serializer.errors)
        

    def delete(self, request, pk):
        queryset = GuestRoom.objects.get(id=pk)
        queryset.delete()
        return Response('Data deleted')

# ---------------------------------------------------------------------------------------------- #   








#------------------Group API view----------------#
class GroupApiView(GenericAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
#---------------- ----------------------------# 

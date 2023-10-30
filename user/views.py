from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from .serializers import *
from django.contrib.auth.hashers import make_password
from rest_framework.generics import GenericAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from core.permissions import CustomModelPermission
from django.contrib.auth.models import Group

#############---- For user login authientication(check if the user is valid)--#####
# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(username=email, password=password)
    if user == None:
        return Response('Invalid email or password!')
    else:
        token,_= Token.objects.get_or_create(user=user)
        return Response({'token': token.key}) 
    

####################################
##----- For user registration-------###
#####################################
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    group_id = request.data.get('role')
    # Step 1: Retrieve the group based on the group_id
    try:
        group = Group.objects.get(id=group_id)
    except Group.DoesNotExist:
        return Response('Group does not exist')
    
    password = request.data.get('password')
    request.data['password'] = make_password(password) #make password function changes user password to encrypted
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        # Step 3: Add the user to the group
        user.groups.add(group)
        user.save()
        return Response('User created and added to the group!')
    else:
        return Response(serializer.errors)
    
class UserApi(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [CustomModelPermission]
    filter_backends =[DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['groups'] 

    def get(self, request):
        queryset = self.get_queryset()
        filter_queryset = self.filter_queryset(queryset)
        serializer = self.serializer_class(filter_queryset, many=True)
        return Response(serializer.data)
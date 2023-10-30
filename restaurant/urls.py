from django.urls import path
from .views import *

urlpatterns =[
    path('menuinfo/all/', MenuSerializerApiView.as_view(), name='menuinfo'),
    path('menu/<int:pk>/', MenuSerializerIdApiView.as_view(), name='menuinfoid'),
    path('foodinfo/all/', FoodSerializerApiView.as_view(), name='foodinfo'),
    path('foodinfo/<int:pk>/', FoodSerializerIdApiView.as_view(), name='foodinfo'),
]


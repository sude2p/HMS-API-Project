from django.urls import path
from .views import *


urlpatterns = [ 
    path('billinfo/all/', BillSerializerView.as_view(), name='billinfo'),
    path('billinfo/<int:pk>/', BillSerializerIdApiView.as_view(), name='billinfoid'),
    path('paymentinfo/all/', PaymentSerializerView.as_view(), name ='paymentinfo' ),
    path('paymentinfo/<int:pk>/', PaymentSerializerIdApiView.as_view(), name='paymentinfoid'),

    
]

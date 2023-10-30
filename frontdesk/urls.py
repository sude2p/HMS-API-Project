from django.urls import path
from .views import*

urlpatterns =[
    path('guestinfo/all/', GuestInfoApiView.as_view(), name='guestinfo'),
    path('guestinfo/<int:pk>/', GuestInfoIdApiView.as_view(), name='guestinfoid'),
    path('group/all/', GroupApiView.as_view(), name='group'),
    path('roomtype/all/', RoomTypeApiView.as_view(), name='roomtype'),
    path('roomtype/<int:pk>/',RoomTypeIdApiVieww.as_view(), name='roomtypeid' ),
    path('roominfo/all/', RoomApiView.as_view(), name='roominfo'),
    path('roominfo/<int:pk>/', RoomApiIdView.as_view(), name='roominfoid'),
    path('guestroominfo/all/', GuestRoomApiView.as_view(), name='guestroominfo'),
    path('guestroominfo/<int:pk>/', GuestRoomApiIdView.as_view(), name='guestroomid')

]
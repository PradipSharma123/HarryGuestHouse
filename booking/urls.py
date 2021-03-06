from django.urls import path
from .views import RoomList, BookingList, BookingView

app_name = 'booking'
urlpatterns = [
    path('room_list/', RoomList.as_view(), name='RoomList'),  # 3   5:30
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('book/', BookingView.as_view(), name='BookingView')

]

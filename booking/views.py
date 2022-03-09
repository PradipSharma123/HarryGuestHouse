from urllib import request
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView
from .models import Room, Booking
from .forms import Availability_rooms
from booking.booking_functions.availability import check_availability

# yeniharu class chai Room ra Booking access garna, admin mai nagai garnako lagi
# I mean admin mai gayerai garna parxa vanni haina nagai pani garna milni banauna ko lagi


class RoomList(ListView):
    model = Room


class BookingList(ListView):
    model = Booking


class BookingView(FormView):
    form_class = Availability_rooms  # imported from forms.py
    template_name = 'hotel.html'

    # THIS IS THE FUCNTION WHICH IS RUN AFTER DJANOG HAS CHECKED IF THE FORM IS VALID 'form_valid'
    def form_valid(self, form):
        data = form.cleaned_data  # Taking the data from the form
        # its imported form the form.py where room category can be related #3 20:00
        # everything from here is imported from availability.py, its all the availability logic used here
        # category is of the model but the room_categoy is form the form.py
        # its is for choosing the category by the customer for eg: if the customer chooses for AC room then they gets the AC room choosen
        room_list = Room.objects.filter(category=data['room_category'])
        available_rooms = []
        for room in room_list:  # it is for running check availability function in each and every room of this list
            # we used check_in to extract check_in from the dictionary, data is already mentioned above. may be it used data cause check_in data is in date format, its just the theory tho
            # if its true then its gonna append the room may be from the available_room list
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)
        if len(available_rooms) > 0:  # available rooms is greater than 0 means, if the room is available, in this case we gonna run this code else we gonna redirect the http response message as mentioned below
            # its the first room that is available from the list
            room = available_rooms[0]
            booking = Booking.objects.create(
                user=self.request.user,  # passing everything that the booking needs its using self.request may be cause we gonna choose the user or sign up as the new user or something going around there, its just the theory tho
                room=room,  # same as from line 40
                check_in=data['check_in'],  # same as mentionde in the line 36
                check_out=data['check_out']
            )  # this all data is returned only the if function is true or the room is empty or available else if the room is not available we gonna redirect the page to something else as mentionde in line 50
            booking.save()
            return(HttpResponse(booking))
        else:
            return(HttpResponse('All of this category of the rooms are already booked !! Try to book by choosing other room category '))
            # after completing this linking this entire Booking_view in our urls.py of app/ creating template to view everything that is going around in it
            # to do that we have to import Booking view from the views.py

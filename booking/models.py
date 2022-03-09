from django.db import models
from django.conf import settings


class Room(models.Model):
    Room_category = (
        ('NAC', 'NON-AC'),
        ('YAC', 'AC'),
    )
    Room_number = models.IntegerField()
    category = models.CharField(max_length=3, choices=Room_category)
    beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.Room_number}. {self.category} of {self.beds} beds with {self.capacity} people'


class Booking(models.Model):
    # foreignkey ra tesko parenthesis vitra vako sabai ko barema herna xa hai aru sab bujexas taile
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user} booked {self.room} in {self.check_in} to {self.check_out}.'

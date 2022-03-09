
from django import forms


class Availability_rooms(forms.Form):
    Room_category = (
        ('NAC', 'NON-AC'),
        ('YAC', 'AC'),
        ('KNG', 'KING'),
        ('QUE', 'QUEEN'),
        ('DEL', 'DELUXE')
    )
    room_category = forms.ChoiceField(choices=Room_category, required=True)
    check_in = forms.DateField(
        required=True, input_formats=["%Y-%m-%d", ])  # you can input any date time module you like from the djano date and time documentation
    check_out = forms.DateField(
        required=True, input_formats=["%Y-%m-%d", ])  # from the official django documentation go the input format that you required

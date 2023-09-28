from rest_framework import serializers
from movie.models import Booking
from tickets.models import Tickets

def validate(self, data):
    seat = data['seats']
    show_time = data['showtime']

    if Booking.objects.filter(seat=seat, show_time=show_time).exists():
        raise serializers.ValidationError({"messege": "Это место уже забранировано!"})

    if Tickets.objects.filter(seats=seat, showtime=show_time).exists():
        raise serializers.ValidationError({"messege": "Это место уже куплено!"})

    return data
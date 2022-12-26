from rest_framework import serializers

from .models import *


class bookingserialzer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields = "__all__"
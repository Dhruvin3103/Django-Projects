from rest_framework import serializers

from .models import *


class paymentserialzer(serializers.ModelSerializer):
    class Meta:
        model = payment
        fields = "__all__"
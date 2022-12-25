from rest_framework import serializers

from .models import *


class theatreserialzer(serializers.ModelSerializer):
    class Meta:
        model = theatre
        fields = "__all__"
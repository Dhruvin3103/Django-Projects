from rest_framework import serializers

from .models import *

class movieserialzer(serializers.ModelSerializer):
    class Meta:
        model = movie
        fields = "__all__"
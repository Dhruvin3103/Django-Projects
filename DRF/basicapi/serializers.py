from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import article


class articleserializer(serializers.ModelSerializer):
    class Meta:
        model = article
        fields = "__all__"

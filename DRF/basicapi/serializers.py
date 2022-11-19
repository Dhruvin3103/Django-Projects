from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import article,movie


class movieserializer(serializers.ModelSerializer):
    class Meta:
        model = movie
        fields = [
            'id',
            'title',
            'content',
            'price',
            # 'sale_price'
        ]

class articleserializer(serializers.ModelSerializer):
    class Meta:
        model = article
        fields = "__all__"

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import article

class articleserializer(serializers.Serializers):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    date = serializers.DateTimeField()

    def create(self, validated_data):
        return article.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance

from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import article,movie
from django.contrib.auth import get_user_model
User = get_user_model()


class signupserialzer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)
    is_verfied = serializers.BooleanField(default=False)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
            'is_verfied',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }
    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        password2 = validated_data.get('password2')


        if password == password2:
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            return user
        else:
            raise serializers.ValidationError({'error':'Both passwords do not match'})

class verifyserialzer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    otp = serializers.CharField(required=True)
# class user_create(U)

class movieserializer(serializers.ModelSerializer):
    class Meta:
        model = movie
        fields = [
            'id',
            'title',
            'content',
            'price',
            'sale_price'
        ]

class articleserializer(serializers.ModelSerializer):
    class Meta:
        model = article
        fields = "__all__"

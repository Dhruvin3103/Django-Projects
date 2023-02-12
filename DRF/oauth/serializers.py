import os

from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from . import google
from .models import *

class GoogleSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate_auth_token(self,auth_token):
        user_data = google.Google.validate(auth_token)
        try:
            user_data['sub']
        except:
            raise serializers.ValidationError("the token is invalid or expired")

        if user_data['aud'] !=os.environ.get('GOOGLE_CLIENT_ID'):
            raise AuthenticationFailed('who are you ?')

        user_id = user_data['sub']
        email = user_data['email']
        name = user_data['name']
        provider = 'google'



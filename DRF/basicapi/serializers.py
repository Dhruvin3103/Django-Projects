from django.contrib.auth.models import Group
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes,smart_str
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from rest_framework import serializers
from django.contrib.auth import get_user_model

from .emails import send_passreset_email

User = get_user_model()

class loginserializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=255)
    class Meta:
        model = User
        fields =['username','password']

class signupserialzer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)
    mob = serializers.IntegerField(required=True,write_only=True)
    age = serializers.IntegerField(required=True,write_only=True)
    is_verfied = serializers.BooleanField(default=False)
    is_theatre_operator = serializers.BooleanField(default=False)
    is_movie_operator = serializers.BooleanField(default=False)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'password2',
            'mob',
            'age',
            'is_verfied',
            'is_theatre_operator',
            'is_movie_operator'
        ]

        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }
    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        password = validated_data.get('password')
        password2 = validated_data.get('password2')
        mob = validated_data.get('mob')
        age = validated_data.get('age')



        if password == password2:
            user = User(username=username, email=email, first_name=first_name, last_name=last_name, mob=mob,age=age)
            user.set_password(password)
            user.save()
            return user
        else:
            raise serializers.ValidationError({'error':'Both passwords do not match'})

class verifyserialzer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    otp = serializers.CharField(required=True)

class change_passwordserializer(serializers.Serializer):
    password = serializers.CharField(max_length=250, style={'input_type':'password'},write_only=True,required=True)
    password2 = serializers.CharField(max_length=250, style={'input_type':'password'},write_only=True,required=True)

    class Meta:
        fields = ['password', 'password2']

        def create(self, r):
            password = r.get('password')
            password2 = r.get('password2')

            if password != password2:
                raise serializers.ValidationError("Passwords are not matching")

            return r

class SendPasswordResetEmailSerializer(serializers.Serializer):
  email = serializers.EmailField(max_length=255)
  class Meta:
    fields = ['email']

  def validate(self, attrs):
    email = attrs.get('email')
    if User.objects.filter(email=email).exists():
      user = User.objects.get(email = email)
      uid = urlsafe_base64_encode(force_bytes(user.id))
      print('Encoded UID', uid)
      token = PasswordResetTokenGenerator().make_token(user)
      print('Password Reset Token', token)
      link = 'http://localhost:8000/api/movie/changepass/'+uid+'/'+token
      print('Password Reset Link', link)
      # Send EMail
      send_passreset_email(email,link)

      # Util.send_email(data)
      return attrs
    else:
      raise serializers.ValidationError('You are not a Registered User')
# class user_create(U)



import os
import random

from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from DRF.basicapi.models import User


def generateUsername(name):
    username = "".join(name.split(' ')).lower()
    if not User.objects.filter(username=username).exists():
        return username
    else:
        random_username = username +"ran"+str(random.randint(0,1000))
        return generateUsername(random_username)

def registerUser(userid,email):
    userbyemail = User.objects.filter(email=email)

    if userbyemail.exists():
        registereduser = authenticate(email=email,password=os.environ.get('SOCIAL_SECRET'))

        return {
            'username' : registereduser.username,
            'email': registereduser.email,
            'tokens': registereduser.tokens()}
    else:
        raise AuthenticationFailed



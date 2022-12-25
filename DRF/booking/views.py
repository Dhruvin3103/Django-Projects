from django.shortcuts import render
from rest_framework import generics

# from .models import *
from ..theatre.models import theatre
# Create your views here.

class theatre_retrieve_create_view(generics.ListCreateAPIView):
    queryset = theatre.objects.all()
    serializer_class =

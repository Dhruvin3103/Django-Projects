from django.shortcuts import render
from rest_framework import mixins, generics, authentication

from .models import *
from .serializers import *


# Create your views here.
class moviemixin(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = movie.objects.all()
    serializer_class = movieserialzer
    authentication_classes = [authentication.TokenAuthentication]

    def get(self,request,*args,**kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

movie_M = moviemixin.as_view()

class movie_retrieve_create_view(generics.ListCreateAPIView):
    queryset = movie.objects.all()
    serializer_class = movieserialzer
    authentication_classes = [
        authentication.TokenAuthentication
    ]

    def perform_create(self, serializer):
        serializer.save()

movie_RC = movie_retrieve_create_view.as_view()
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, authentication, mixins
from .models import *
from .serializers import *
from DRF.permissions import theatrepermission


class theatremixin(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = theatre.objects.all()
    serializer_class = theatreserialzer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [theatrepermission]
    def get(self,request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request)
    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request, *args, **kwargs)

theatreM = theatremixin.as_view()
class theatre_retrieve_create_view(generics.ListCreateAPIView):
    queryset = theatre.objects.all()
    serializer_class = theatreserialzer
    authentication_classes = [
        authentication.TokenAuthentication
    ]
    permission_classes = [theatrepermission]

    def perform_create(self, serializer):
        serializer.save()

theatre_RC = theatre_retrieve_create_view.as_view()


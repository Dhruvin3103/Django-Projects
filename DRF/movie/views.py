from datetime import date

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.utils.datetime_safe import datetime
from rest_framework import mixins, generics, authentication
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *
from DRF.permissions import moviepermission


# Create your views here.
class moviemixin(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
    PermissionRequiredMixin
):
    queryset = movie.objects.all()
    serializer_class = movieserialzer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [moviepermission]

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

# class movie_retrieve_create_view(generics.ListCreateAPIView):
#     queryset = movie.objects.all()
#     serializer_class = movieserialzer
#     authentication_classes = [
#         authentication.TokenAuthentication
#     ]
#
#     def perform_create(self, serializer):
#         serializer.save()


class create_movie_view(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [moviepermission]
    def get(self,request):
        data = movie.objects.all()
        d = [i for i in movie.objects.all().values()]

        # if((d[0]['movie_time'].date())<date(2022,12,26)):print(1)
        serializer = movieserialzer(data,many=True)
        return Response({
            'status':200,
            'data':serializer.data
        })

    def post(self,request):
        try:
            data = request.data
            d = data['movie_time']
            id=data['theatre_no']
            t = theatre.objects.filter(id=id).values()
            m = movie.objects.filter(theatre_no=id)
            m1 = movie.objects.filter(movie_time=data['movie_time'])
            c=0
            print(m1.count())

            data['hall_no']=m.count()+1
            if(t[0]['no_of_halls'] >m1.count()):
                serializer = movieserialzer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({
                        'status':200,
                        'message':'movie is regristered to this theatre',
                        'data':serializer.data,
                    })
                else:
                    return Response({
                        'status':400,
                        'message':'error occured',
                        'data':serializer.errors,
                    })
            else:
                return Response({
                    'status':400,
                    'message':'all slots are booked try for other day'
                })
        except Exception as e:
            print(e)
movie_RC = create_movie_view.as_view()
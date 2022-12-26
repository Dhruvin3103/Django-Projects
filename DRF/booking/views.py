from django.shortcuts import render

from rest_framework import mixins, generics, authentication
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *



class bookingmixin(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = booking.objects.all()
    serializer_class = bookingserialzer
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


booking_m = bookingmixin.as_view()


class create_booking(APIView):

    def get(self,request):
        data = booking.objects.all()
        d = [i for i in booking.objects.all().values()]
        print(data.count())
        serializer = bookingserialzer(data,many=True)
        return Response({
            'status':200,
            'data': serializer.data
        })
    def post(self,request):
        try:
            data = request.data
            t=data['b_no_of_tickets']
            id=data['movie_no']
            m= movie.objects.filter(id=id).values()
            d = booking.objects.filter(movie_no=id)
            p=m[0]['movie_ticket_price']*t
            data['booking_price']=p
            print(m[0]['no_of_seats'])
            c = 0
            for i in d.values(): c = c+i['b_no_of_tickets']
            print(c)
            # print(x)
            if((m[0]['no_of_seats']-c)>=data['b_no_of_tickets']):
                serializer = bookingserialzer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(
                        {
                            'status':200,
                            'message':'booking completed you can proceed for payment',
                            'data':serializer.data,
                        }
                    )
                else:
                    return Response({
                        'status':400,
                        'message':'error occured',
                        'data':serializer.errors,
                    })
            else:
                return Response({
                    'status':400,
                    'message':'Housefull sry :(',
                })
        except Exception as e:
            print(e)

create_b = create_booking.as_view()

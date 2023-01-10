from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import authentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
import razorpay
from .serializers import paymentserialzer
from django.conf import settings
from .models import *



#  @csrf_exempt
# @api_view(['POST'])
# def payment(request):
#     if request.method == "POST":
#         data = request.data
#         id = data['p_booking_id']
#         data1 = booking.objects.filter(id=id).values()
#         print(data1[0]['booking_price'])
#         print(data1[0]['booking_price'])
#         data['p_price'] = data1[0]['booking_price']
#         print(data['p_price'])
#         k = settings.RAZORPAY_KEY_ID
#         print(k)
#         client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
#         order = client.order.create(
#             {"amount": data['p_price'] * 100,
#              "currency": "INR",
#              "payment_capture": "1"}
#         )
#         serializer = paymentserialzer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return render(
#                 request,
#                 "payment.html",
#                 {
#                     "razor_key": k,
#                     "amount": serializer.data['p_price'],
#                     "booking_id": serializer.data['p_booking_id'],
#                     "name": order['id']
#                 }
#             )
#         else:
#             return Response({
#                 'status': 400,
#                 'message': 'error occured',
#                 'data': serializer.errors,
#             })
#
# Create your views here.
class payment(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    def post(self,request):

            data = request.data
            id = data['p_booking_id']
            data1 = booking.objects.filter(id=id).values()
            print(data1[0]['booking_price'])
            data['p_price'] = data1[0]['booking_price']
            print(data['p_price'])
            k = settings.RAZORPAY_KEY_ID
            print(k)
            client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
            order = client.order.create(
                {"amount" : data['p_price']*100,
                 "currency": "INR",
                 "payment_capture": "1"}
            )
            serializer = paymentserialzer(data=data)
            if serializer.is_valid():
                serializer.save()
                return render(
                    request,
                    "payment.html",
                    {
                        "razor_key" : k,
                        "amount" : serializer.data['p_price'],
                        "booking_id" : serializer.data['p_booking_id'],
                        "name": order['id']
                    }
                )
            else:
                return Response({
                    'status': 400,
                    'message': 'error occured',
                    'data': serializer.errors,
                })
        # except Exception as e:
        #     return Response({
        #         'message':'error occurred'
        #     })

payment = payment.as_view()
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# rest_framework import
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import article, movie
from .serializers import articleserializer,movieserializer
import json


@api_view(["POST"])
def apihome(request, *args, **kwargs):
    print(request.data)
    serial = movieserializer(data=request.data)
    if serial.is_valid(raise_exception=True):
        serial.save()
        print(serial.data)
    # instance = movie.objects.all().order_by("?").first()
    # data={}
    # if instance:
    #     data = movieserializer(instance).data
        return Response(serial.data)


# Create your views here.
@csrf_exempt
def alist(request):
    if request.method == "GET":
        art = article.objects.all()
        serial = articleserializer(art, many=True)
        return JsonResponse(serial.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serial = articleserializer(data=data)

        if serial.is_valid():
            serial.save()
            return JsonResponse(serial.data, status=201)
        return JsonResponse(serial.errors, status=400)


@csrf_exempt
def adetail(request, pk):
    try:
        art = article.objects.get(pk=pk)

    except article.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serial = articleserializer(art)
        return JsonResponse(serial.data, safe=False)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serial = articleserializer(art, data=data)
        if serial.is_valid():
            serial.save()
            return JsonResponse(serial.data)
        return JsonResponse(serial.errors, status=400)

    elif request.method == "DELETE":
        art.delete()
        return HttpResponse(status=204)

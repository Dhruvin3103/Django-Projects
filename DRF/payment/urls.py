from django.urls import path
from . import views

urlpatterns =[
    path('',views.input, name ='input'),
    path('pay/',views.payment, name ='payment'),
]
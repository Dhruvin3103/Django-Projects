from django.urls import path
from . import views

urlpatterns =[
    # path('retrivecreate/',views._RC, name ='movieRC'),
    path('mixin/<int:pk>',views.booking_m, name ='booking_m'),
    path('create/',views.create_b, name ='booking_c'),
]
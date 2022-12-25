from django.urls import path
from . import views

urlpatterns =[
    path('retrivecreate/',views.movie_RC, name ='movieRC'),
    path('mixin/<int:pk>',views.movie_M, name ='movie_m'),
]
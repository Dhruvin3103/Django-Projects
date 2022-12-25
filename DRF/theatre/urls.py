from django.urls import path
from . import views

urlpatterns =[
    path('retrivecreate/',views.theatre_RC, name ='theatreRC'),
    # path('<int:pk>/update/',views.theatre_U, name ='theatreU'),
    # path('<int:pk>/update/',views.theatre_U, name ='theatreU'),
    path('mixin/<int:pk>',views.theatreM, name ='theatreM'),
]
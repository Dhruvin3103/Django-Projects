from django.urls import path
from . import views
urlpatterns = [
    path('', views.moviecreateview, name ='moviecreate'),
    path('<int:pk>/', views.movieview, name ='movieview'),
    path('<int:pk>/update/', views.movieupdateview, name ='movieview'),
    path('<int:pk>/delete/', views.moviedeleteview, name ='movieview'),


    path('art/', views.alist, name ='art'),
    path('apihome/', views.apihome, name ='apihome'),
    path('artdet/<int:pk>/', views.adetail, name ='artdet')
    # path('api-auth/', include('rest_framework.urls'))
]
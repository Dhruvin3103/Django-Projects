from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    # path('', views.moviecreateview, name ='moviecreate'),
    # path('<int:pk>/', views.movieview, name ='movieview'),
    # path('<int:pk>/update/', views.movieupdateview, name ='movieview'),
    # path('<int:pk>/delete/', views.moviedeleteview, name ='movieview'),
    path('signup/', views.signupapi, name ='signupapi'),
    path('verify/', views.verify, name ='verify'),
    path('login/', views.login1, name ='login'),
    path('changepass/', views.change_pass, name ='change_pass'),

    path('auth/', obtain_auth_token, name ='auth'),
    # path('art/', views.alist, name ='art'),

    # path('apihome/', views.apihome, name ='apihome'),
    # path('artdet/<int:pk>/', views.adetail, name ='artdet')
    # path('api-auth/', include('rest_framework.urls'))
]
from django.urls import path
from . import views
urlpatterns = [
    path('art/', views.alist, name ='art'),
    path('apihome/', views.apihome, name ='apihome'),
    path('artdet/<int:pk>/', views.adetail, name ='artdet')
    # path('api-auth/', include('rest_framework.urls'))
]
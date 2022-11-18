from django.urls import path
from .views import alist,adetail
urlpatterns = [
    path('art/', alist, name ='art'),
    path('artdet/<int:pk>/', adetail, name ='artdet')
    # path('api-auth/', include('rest_framework.urls'))
]
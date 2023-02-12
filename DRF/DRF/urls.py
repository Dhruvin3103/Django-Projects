"""DRF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from django.contrib import admin
from django.urls import path, include
from basicapi import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/movie/', include('basicapi.urls')),
    path('api/theatre/',include('theatre.urls')),
    path('api/movie/',include('movie.urls')),
    path('api/booking/',include('booking.urls')),
    path('api/payment/',include('payment.urls')),
    path('accounts/',include('allauth.urls')),
    path('openapi', get_schema_view(
        title="Your Project",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema'),
    path('', TemplateView.as_view(
        template_name='swagger.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swaggerui'),
    path('oauth/',TemplateView.as_view(template_name='index.html')),
    # path('api-auth/', include('rest_framework.urls'))
]

"""todolist URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from todoL import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('',views.home1,name='home1'),
    path('create/',views.create,name='create'),
    path('task/',views.task,name='task'),
    path('retriveT/',views.retrive,name='retrive'),
    path('retriveL/<str:id>',views.retriveL,name='retriveL'),
    path('checkbox/',views.checkbox,name='checkbox'),
    path('checkbox1/',views.checkbox1,name='checkbox1'),
    # path('radio1/',views.radio1,name='radio1'),
    path('deleteT/',views.delete_task,name='deleteT'),
    path('deleteL/',views.delete_list,name='deleteL'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('updateL/<int:id1>',views.update_list,name='updateL'),
    path('updateT/<int:id2>/<int:id3>',views.update_task,name='updateT'),
    # path('update2/<int:id>',views.update2,name='update2'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
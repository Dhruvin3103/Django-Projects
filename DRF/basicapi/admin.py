from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(theatreUser)


class useradmin(admin.ModelAdmin):
    filter_horizontal = ("groups", "user_permissions")

admin.site.register(User,useradmin)
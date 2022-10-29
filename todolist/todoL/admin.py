from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .form import user_createform,user_changeform

# Register your models here.
from .models import user
from .models import Task
from .models import List

class user_admin(UserAdmin):
    add_form = user_createform
    form = user_changeform
    model = user

    list_display = ['username', 'mob_no', 'dob']
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('mob_no', 'dob')}),)



admin.site.register(user,user_admin)
admin.site.register(Task)
admin.site.register(List)

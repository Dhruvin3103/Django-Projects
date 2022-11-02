from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .form import user_createform,user_changeform

# Register your models here.
from .models import *

class listadmin(admin.ModelAdmin):
    # exclude = ('task_FK',)
    list_display = ('title1','start','end','taskc','statusc')
    list_display_links = ('title1','taskc',)
    list_filter = ('start','end','status')
    list_per_page = 10
    radio_fields = {'status': admin.HORIZONTAL}
    save_on_top = True
    def statusc(self , obj):
        return format_html(f'<span style="color:red">{obj.status}</span>')

    def taskc(self , obj):
        return format_html(f'<a href ="http://127.0.0.1:8000/admin/todoL/task/{obj.id}/change/"><span '
                           f'style="color:purple">{obj.task_FK}</span></a>')
class user_admin(UserAdmin):
    add_form = user_createform
    form = user_changeform
    model = user
    readonly_fields = ('img',)
    list_display = ['username','email', 'mob_no', 'dob', 'imgs','img']
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('mob_no', 'dob', 'imgs','img')}),)

    def img(self,obj):
        return format_html(f'<img src="/media/{obj.imgs}" style="height:10px;width:10px')


admin.site.register(user,user_admin)
admin.site.register(Task)
admin.site.register(List,listadmin)

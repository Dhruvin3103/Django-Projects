from django import forms
from .models import List,Task,user
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
class user_createform(UserCreationForm):
    class Meta:
        model = user
        fields = ('username','mob_no','dob')

class user_changeform(UserChangeForm):
    class Meta:
        model = user
        fields = ('username','mob_no','dob')

class Createview(forms.ModelForm):
    class Meta:
        model = List
        fields ='__all__'

class Taskview(forms.ModelForm):
    class Meta:
        model = Task
        fields = {
            'title'
        }
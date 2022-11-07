from django import forms
from email.mime import image
from .models import List,Task,user
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
class user_createform(UserCreationForm):
    class Meta:
        model = user
        fields = ('username','email','password1','password2','mob_no','dob','imgs')

class user_changeform(UserChangeForm):
    class Meta:
        model = user
        fields = ('username','email','mob_no','dob','imgs')

class Createview(forms.ModelForm):
    class Meta:
        model = List
        fields ='__all__'

class Taskview(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

class image(forms.Form):
    image = forms.ImageField()
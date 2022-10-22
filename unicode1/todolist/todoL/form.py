from django import forms

from .models import List,Task

class Createview(forms.ModelForm):
    class Meta:
        model = List
        fields ='__all__'

class Taskview(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
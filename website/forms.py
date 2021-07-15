from django import forms
from .models import Content

class ContentForm(forms.ModelForm):
    class meta:
        model = Content
        fields = ['name','data_posted']
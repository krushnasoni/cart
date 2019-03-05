from django import forms
from .models import Category

class CatForm(forms.ModelForm):

    class Meta:
            model = Category
            fields = ['name']

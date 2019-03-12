from django import forms
from .models import Products

class ProdForm(forms.ModelForm):

    class Meta:
            model = Products
            exclude = ['image','admin','created_date']

class ImageFileUploadForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('image',)
        exclude = ['price','admin_id']


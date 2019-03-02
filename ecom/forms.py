from django import forms
from .models import Users

class SignUpForm(forms.ModelForm):

    class Meta:
            model = Users
            fields = ('username', 'password', 'email')
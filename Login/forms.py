from django import forms

from .models import UserModel

class RegisterModelForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'password']

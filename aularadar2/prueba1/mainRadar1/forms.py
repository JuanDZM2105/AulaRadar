from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import comentario

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','first_name','last_name','email','password1','password2']



class ComentarioForm(forms.ModelForm):
    class Meta:
        model = comentario
        fields = ['descripcion']

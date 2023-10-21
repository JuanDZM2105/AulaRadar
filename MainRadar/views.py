from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import universidad
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import datetime


# Create your views here.
def home(request):
    return render(request, 'home.html')

def exit(request):
    logout(request)
    return redirect('home')
 
@login_required
def main(request):
    universidades = universidad.objects.all()
    return render(request, 'main.html',{ 'universidades':universidades})

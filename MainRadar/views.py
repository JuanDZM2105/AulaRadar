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
    searchTerm=request.GET.get('searchUniversity')
    if searchTerm:
        universidades=universidad.objects.filter(nombre__icontains=searchTerm)
        return render(request, 'main.html',{ 'searchTerm':searchTerm, 'universidades':universidades})
    else:  
        return render(request, 'main.html')

def more_info(request,id_unico):
    universidad1 = get_object_or_404(universidad, id_unico=id_unico)
    

   
    

    return render(request, 'more_info.html', {'universidad': universidad1})

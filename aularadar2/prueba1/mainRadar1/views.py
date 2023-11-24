from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import universidad,curso,programa_academicos, curso_programa,comentario
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import datetime
from .forms import CustomUserCreationForm, ComentarioForm
from django.contrib.auth import authenticate, login
from abc import ABC, abstractmethod









# Create your views here.
def home(request):
    return render(request, 'home.html')

def exit(request):
    logout(request)
    return redirect('home')

class Buscador(ABC):
    @abstractmethod
    def buscar(self, searchTerm):
        pass

class BuscadorUniversidad(Buscador):
    def buscar(self, searchTerm):
        universidades = universidad.objects.filter(nombre__icontains=searchTerm)
        return universidades, 1

class BuscadorPrograma(Buscador):
    def buscar(self, searchTerm):
        programas = programa_academicos.objects.filter(nombre__icontains=searchTerm)
        universidades = []
        for programa in programas:
            universidad1 = universidad.objects.filter(id_unico__icontains=programa.id_universidad.id_unico).first()
            universidades.append(universidad1)
        return zip(universidades, programas), 2

class BuscadorPorTipo(Buscador):
    def buscar(self, searchTerm):
        universidades = universidad.objects.filter(tipo__icontains=searchTerm)
        return universidades, 1

class BuscadorPorUbicacion(Buscador):
    def buscar(self, searchTerm):
        universidades = universidad.objects.filter(ubicacion__icontains=searchTerm)
        return universidades, 1

@login_required
def main(request):
    searchTerm = request.GET.get('searchUniversity')
    search = request.GET.get('busqueda')
    tipo = request.GET.get('tipo')
    ubicacion = request.GET.get('ubicacion')
    buscador = None
    busqueda = None
    aux = None
    if searchTerm:
        if search == "universidad":
            buscador = BuscadorUniversidad()
        elif search == "programa":
            buscador = BuscadorPrograma()
        if buscador:
            busqueda, aux = buscador.buscar(searchTerm)
            if tipo != "NULL":
                busqueda = busqueda.filter(tipo=tipo)
            if ubicacion != "NULL":
                busqueda = busqueda.filter(ubicacion=ubicacion)
    else:  
        if search == "universidad":
            busqueda = universidad.objects.all()
            aux = 1
            if tipo != "NULL":
                busqueda = busqueda.filter(tipo=tipo)
            if ubicacion != "NULL":
                busqueda = busqueda.filter(ubicacion=ubicacion)
        
              
        
    return render(request, 'main.html', { 'searchTerm':searchTerm, 'busqueda':busqueda ,'aux':aux })
    

    
def more_info(request, id_unico):
    universidad_obj = get_object_or_404(universidad, id_unico=id_unico)
    comentarios = comentario.objects.filter(id_universidad=id_unico)
    programas_academicos = programa_academicos.objects.filter(id_universidad=id_unico)  # Nueva línea

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            nuevo_comentario = form.save(commit=False)
            nuevo_comentario.id_usuario = request.user
            nuevo_comentario.id_universidad = universidad_obj
            nuevo_comentario.id_unico3 = comentario.objects.count() + 1
            nuevo_comentario.save()
    else:
        form = ComentarioForm()

    return render(request, 'more_info.html', {'universidad': universidad_obj, 'comentarios': comentarios, 'form': form, 'programas_academicos': programas_academicos})  # Modificado

def more_info_programa(request, id_unico):
    programa_obj = get_object_or_404(programa_academicos, id_unico=id_unico)
    comentarios = comentario.objects.filter(id_programa_academico=id_unico)
    cursos_programas = curso_programa.objects.filter(id_programa_academico=id_unico)  # Nueva línea
    cursos = [cp.id_curso for cp in cursos_programas]  # Nueva línea

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            nuevo_comentario = form.save(commit=False)
            nuevo_comentario.id_usuario = request.user
            nuevo_comentario.id_programa_academico = programa_obj
            nuevo_comentario.id_unico3 = comentario.objects.count() + 1
            nuevo_comentario.save()
    else:
        form = ComentarioForm()

    return render(request, 'more_info_programa.html', {'programa': programa_obj, 'comentarios': comentarios, 'form': form, 'cursos': cursos})  # Modificado

def register(request):  
    data = {'form':CustomUserCreationForm()}
    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            user= authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect('main')
        else:
            data["form"] = formulario
    return render(request, 'registration/register.html', data)







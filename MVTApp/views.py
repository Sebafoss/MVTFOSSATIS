from django.shortcuts import render

# Create your views here.

from MVTApp.models import Familiares

def mostrar_Familiares(request):
    
    F1 = Familiares(nombre= 'Carlos', apellido='Fossati', edad=75, nacimiento= '1947-6-28', Email= 'Carlosfossati@gmail.com')
    F2 = Familiares(nombre='Isabel', apellido= 'Diaz', edad= 73, nacimiento= '1949-8-30', Email= 'isadiaz2020@gmail.com') 
    F3 = Familiares(nombre='Diego', apellido= 'Fossati', edad= 48, nacimiento= '1974-12-10', Email= 'diegofoss@yahoo.com.ar')

    return render(request,'MVTApp/Familiares.html', {'Familiares':[F1, F2, F3]})
from django.shortcuts import render,redirect
from .models import Task


def task_one(request):
    info = Task.objects.all()
    return render(request,'index.html',{"info": info})

def create_task(request):
    ctask = Task(codigo=request.POST['codigo'],nif=request.POST['nif'],nombre=request.POST['nombre'],
                 apellido1=request.POST['apellido1'],apellido2=request.POST['apellido2'],codigo_departamento=request.POST['codigo_departamento'])
    ctask.save()
    return redirect('/hello/')

def delete(request,iddb):
    ctask = Task.objects.get(id=iddb)
    ctask.delete()
    print(id)
    return redirect('/hello/')

def update(request, iddb):
    ctask = Task.objects.get(id=iddb)
    return render(request,"update.html",{"ctask":ctask})

def finalupdate(request,iddb):
    codigo=request.POST['codigo']
    nif=request.POST['nif']
    nombre=request.POST['nombre']
    apellido1=request.POST['apellido1']
    apellido2=request.POST['apellido2']
    codigo_departamento=request.POST['codigo_departamento']
    ctask = Task.objects.get(id=iddb)
    ctask.codigo = codigo
    ctask.nif    = nif
    ctask.nombre = nombre
    ctask.apellido1 = apellido1
    ctask.apellido2 = apellido2
    ctask.codigo_departamento = codigo_departamento
    ctask.save()
    return redirect('/hello')
    


# Create your views here.

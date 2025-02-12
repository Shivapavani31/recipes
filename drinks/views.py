from django.shortcuts import render
from .models import *
# Create your views here.
def Milkshakes(request):
    milkshake=milkshakes.objects.all()
    return render(request,'drinks/milkshakes.html',{'milkshake':milkshake})

def showmilkshakes(request,id):
    showmilkshakes=milkshakes.objects.get(id=id)
    return render(request,'drinks/showmilkshakes.html',{'showmilkshakes':showmilkshakes})

def Mojitos(request):
    mojito=mojitos.objects.all()
    return render(request,'drinks/mojitos.html',{'mojito':mojito})

def showmojitos(request,id):    
    showmojitos=mojitos.objects.get(id=id)
    return render(request,'drinks/showmojitos.html',{'showmojitos':showmojitos})

def Juice(request): 
    juices=juice.objects.all()   
    return render(request,'drinks/juice.html',{'juices':juices})  

def showjuice(request,id):
    showjuice=juice.objects.get(id=id)
    return render(request,'drinks/showjuice.html',{'showjuice':showjuice})

def Softdrinks(request):
    softdrink=smooties.objects.all()
    return render(request,'drinks/softdrinks.html',{'softdrink':softdrink})

def showsoftdrinks(request,id):   
    showsoftdrinks=smooties.objects.get(id=id)
    return render(request,'drinks/showsoftdrinks.html',{'showsoftdrinks':showsoftdrinks})
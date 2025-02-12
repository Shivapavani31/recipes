from django.shortcuts import render
from .models import *
# Create your views here.
def Chicken(request):
    curry = chicken.objects.all()
    return render(request,'nonveg/chicken.html',{'curry':curry})

def Showchicken(request,id):
    showchicken=chicken.objects.get(id=id)
    return render(request,'nonveg/showchicken.html',{'showchicken':showchicken})

def Meat(request):
    meats=meat.objects.all()
    return render(request,'nonveg/meat.html',{'meats':meats})

def Showmeat(request,id):
    showmeat=meat.objects.get(id=id)  
    return render(request,'nonveg/showmeat.html',{'showmeat':showmeat})

def Pork(request):
    porks=pork.objects.all()
    return render(request,'nonveg/pork.html',{'porks':porks})

def Showpork(request,id):
    showpork=pork.objects.get(id=id)
    return render(request,'nonveg/showpork.html',{'showpork':showpork})

def Seafood(request):
    seafoods=seafood.objects.all()
    return render(request,'nonveg/seafood.html',{'seafoods':seafoods})

def Showseafood(request,id):
    showseafood=seafood.objects.get(id=id)
    return render(request,'nonveg/showseafood.html',{'showseafood':showseafood})

def Beef(request):  
    beefs=beef.objects.all()
    return render(request,'nonveg/beef.html',{'beefs':beefs})

def Showbeef(request,id):
    showbeef=beef.objects.get(id=id)
    return render(request,'nonveg/showbeef.html',{'showbeef':showbeef})
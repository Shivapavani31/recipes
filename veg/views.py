from django.shortcuts import render
from .models import *
# Create your views here.

def Soups(request):
    soup = soups.objects.all()
    return render(request,'veg1/soups.html',{'soup':soup})

def showsoups(request,id):
    showsoup=soups.objects.get(id=id)
    return render(request,'veg1/showsoups.html',{'showsoups':showsoup})   

def Curries(request):
    curry = curries.objects.all()
    return render(request,'veg1/curries.html',{'curry':curry})

def showcurries(request,id):
    showcurries=curries.objects.get(id=id)
    return render(request,'veg1/showcurries.html',{'showcurries':showcurries})   

def Quickandeasy(request):
    quickandeasys = quickandeasy.objects.all()
    return render(request,'veg1/quickandeasy.html',{'quickandeasys':quickandeasys})

def showquickandeasy(request,id):
    showquickandeasy=quickandeasy.objects.get(id=id)
    return render(request,'veg1/showquickandeasy.html',{'showquickandeasy':showquickandeasy})

def Biryani(request):    
    biryanis = biryani.objects.all()
    return render(request,'veg1/biryani.html',{'biryanis':biryanis})

def showbiryani(request,id):
    showbiryani=biryani.objects.get(id=id)
    return render(request,'veg1/showbiryani.html',{'showbiryanis':showbiryani})

def Fastfood(request):
    fastfoods = fastfood.objects.all()
    return render(request,'veg1/fastfood.html',{'fastfoods':fastfoods})

def showfastfood(request,id):
    showfastfood=fastfood.objects.get(id=id)
    return render(request,'veg1/showfastfood.html',{'showfastfoods':showfastfood})

def Staters(request):    
    staterss = staters.objects.all()
    return render(request,'veg1/staters.html',{'staterss':staterss})

def showstaters(request,id):
    showstaters=staters.objects.get(id=id)
    return render(request,'veg1/showstaters.html',{'showstaters':showstaters})
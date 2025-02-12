from django.shortcuts import render
from .models import *
# Create your views here.
def Chocolate(request):
    chocolates = chocolate.objects.all()
    return render(request,'desserts/chocolate.html',{'chocolates':chocolates})

def Showchocolate(request,id):
    showchocolate=chocolate.objects.get(id=id)
    return render(request,'desserts/showchocolate.html',{'showchocolate':showchocolate})

def Cake(request):
    cakes = cake.objects.all()
    return render(request,'desserts/cake.html',{'cakes':cakes})

def Showcake(request,id):
    showcake=cake.objects.get(id=id)
    return render(request,'desserts/showcake.html',{'showcake':showcake}) 

def Fruits(request):
    fruit = fruits.objects.all()
    return render(request,'desserts/fruits.html',{'fruit':fruit})

def Showfruits(request,id):
    showfruits=fruits.objects.get(id=id)
    return render(request,'desserts/showfruits.html',{'showfruits':showfruits})

def Caramel(request):
    caramels = caramel.objects.all()
    return render(request,'desserts/caramel.html',{'caramels':caramels})

def Showcaramel(request,id):
    showcaramel=caramel.objects.get(id=id)
    return render(request,'desserts/showcaramel.html',{'showcaramel':showcaramel})

def Cookies(request):
    cookie = cookies.objects.all()
    return render(request,'desserts/cookies.html',{'cookie':cookie})  

def Showcookies(request,id):
    showcookies=cookies.objects.get(id=id)
    return render(request,'desserts/showcookies.html',{'showcookies':showcookies})



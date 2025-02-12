from django.shortcuts import render
from.models import *
# Create your views here.
def Idly(request):
    idlys = idly.objects.all()
    return render(request,'tiffins/idly.html',{'idlys':idlys})

def Showidly(request,id):
    showidly=idly.objects.get(id=id)
    return render(request,'tiffins/showidly.html',{'showidly':showidly})    

def Dosa(request):
    dosas = dosa.objects.all()
    return render(request,'tiffins/dosa.html',{'dosas':dosas})

def Showdosa(request,id):
    showdosa=dosa.objects.get(id=id)
    return render(request,'tiffins/showdosa.html',{'showdosa':showdosa})

def Puri(request):
    puris = puri.objects.all()
    return render(request,'tiffins/puri.html',{'puris':puris})

def Showpuri(request,id):
    showpuri=puri.objects.get(id=id)
    return render(request,'tiffins/showpuri.html',{'showpuri':showpuri})

def Upma(request):
    upmas = upma.objects.all()
    return render(request,'tiffins/upma.html',{'upmas':upmas})

def Showupma(request,id):
    showupma=upma.objects.get(id=id)
    return render(request,'tiffins/showupma.html',{'showupma':showupma})

def Poha(request):
    pohas = poha.objects.all()
    return render(request,'tiffins/poha.html',{'pohas':pohas})

def Showpoha(request,id):
    showpoha=poha.objects.get(id=id)
    return render(request,'tiffins/showpoha.html',{'showpoha':showpoha})
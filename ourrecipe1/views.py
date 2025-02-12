from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'Home.html')

def veg(request):
    return render(request,'veg.html')

def nonveg(request):
    return render(request,'nonveg.html')

def dessert(request):
    return render(request,'dessert.html')

def drinks(request):
    return render(request,'drinks.html')

def snacks(request):
    return render(request,'snacks.html')

def tiffins(request):
    return render(request,'tiffins.html')

def calories(request):
    return render(request,'calories.html')
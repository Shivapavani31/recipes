from django.shortcuts import render
from .models import *
# Create your views here.

def Traditionalsnacks(request):
    traditional=traditionalsnacks.objects.all()
    return render(request,'snacks/traditionalsnacks.html',{'traditional':traditional})

def Showtraditionalsnacks(request,id):
    showtraditionalsnacks=traditionalsnacks.objects.get(id=id)
    return render(request,'snacks/showtraditionalsnacks.html',{'showtraditionalsnacks':showtraditionalsnacks})

def Schoolsnacks(request):
    schoolsnack=schoolsnacks.objects.all()
    return render(request,'snacks/schoolsnacks.html',{'schoolsnack':schoolsnack})

def Showschoolsnacks(request,id):    
    showschoolsnacks=schoolsnacks.objects.get(id=id)
    return render(request,'snacks/showschoolsnacks.html',{'showschoolsnacks':showschoolsnacks})

def Timepasssnacks(request):   
    timepass=timepasssnacks.objects.all() 
    return render(request,'snacks/timepasssnacks.html',{'timepass':timepass})

def Showtimepasssnacks(request,id):
    showtimepasssnacks=timepasssnacks.objects.get(id=id)
    return render(request,'snacks/showtimepasssnacks.html',{'showtimepasssnacks':showtimepasssnacks})
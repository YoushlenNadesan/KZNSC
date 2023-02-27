from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest

def personinfo(request):
    return render(request,'personalinformation.html')

def education(request):
    return render(request,'educationinformation.html')

def employment(request):
    return render(request,'employmentinformation.html')

def nextofkin(request):
    return render(request,'nextofkininformation.html')

def cruds(request):
    return render(request,'crud.html')
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):
    products=Product.objects.all()
    #return HttpResponse("<h1>Welcome to django</h1>")
    return render(request,'index.html',{'products':products})

def about(request):
    return HttpResponse("<h1>This is about page</h1>")


def contact(request):
    return HttpResponse("<h1> This is contact page</h1>")
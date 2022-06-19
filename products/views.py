from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Product

# Create your views here.


def index(request):
    products=Product.objects.all()

    return render(request,'index.html',
                  {'products':products}) # here we passed a dictionary named products
                                                               # which take the value of product object


def new(request):
    return HttpResponse("New Products")

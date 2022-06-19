from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("You are on product page")


def new(request):
    return HttpResponse("New Products")

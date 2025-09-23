from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello, this is one line!</h1>")

""" return render(request,"focone.html") """

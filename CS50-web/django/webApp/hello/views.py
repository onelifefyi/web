from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def vapor(request):
    return HttpResponse("Hello, vapor!")

def greet(request, name):
    name = name.capitalize()
    return render(request, "hello/greet.html", {
        "name":name
    })

from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'posts/home.html')
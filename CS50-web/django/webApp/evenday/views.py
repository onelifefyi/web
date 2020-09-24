from django.shortcuts import render
from django.shortcuts import HttpResponse
from datetime import date

# Create your views here.
def index(request):
    day = date.today().day
    return render(request, "evenday/index.html", {
        "day":day
    })
    
from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# Create your views here.

rooms = [
    {'id':1, 'name':'Lets Learn python!'},
    {'id':2, 'name':'Design Patterns'},
    {'id':3, 'name':'Memes!'},
]

def home(request):
    rooms = Room.objects
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = None
    for obj in rooms:
        if obj['id'] == int(pk):
            room = obj

    context = {'room': room}

    return render(request, 'base/room.html', context)
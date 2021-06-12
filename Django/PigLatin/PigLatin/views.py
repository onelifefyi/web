from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello World!")

def home(request):
    return render(request, 'home.html')

def translate(request):
    original = request.GET['originalText']
    original = original.lower()
    translation = ''
    for word in original.split():
        if word[0] in 'aeiou':
            translation += word
            translation += 'yay '
        else:
            translation += word[1:] + word[0] + 'ay '
    return render(request, 'translate.html', {'original':original, 'translation':translation})
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def statement(request):
    return HttpResponse("My name is Raji and Iam new to django")

def routes(request):
    return HttpResponse("This is our routing works in django")

def greetusers(request, name):
    return render(request, 'hello/greet.html', {
        'name': name.capitalize()
    })

#def greetusers(request, name):
 #   return HttpResponse(f'Hello, {name.capitalize()}')
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # return HttpResponse("Hello, Django . This is my project in Django!")
    return render(request, "hello/index.html")

def sayhello(request):
    return HttpResponse("Hello venky!")

def avinash(request):
    return HttpResponse("Hey!, avinash!!")

def greeting(request, name):
    # return HttpResponse(f"Hello!, {name.capitalize()}!...")
    return render(request, "hello/greeting.html", {
        "name" : name.capitalize()
    })
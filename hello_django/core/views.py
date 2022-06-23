from django.shortcuts import render, HttpResponse

# Create your views here.
def helloYou(request, name):
    return HttpResponse(f'<h1>Hello, {name}!</h1>')

def hello(request):
    return HttpResponse('<h1>Hello, world!</h1>')

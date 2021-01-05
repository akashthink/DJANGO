from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def show(request):
    return HttpResponse('<h1 align="center">Welcome to Informatics</h1>')

def show1(request):
    return HttpResponse('<h1 align="center">Welcome to Informatics branch1</h1>')

def show2(request):
    return HttpResponse('<h1 align="center">Welcome to Informatics branch2</h1>')

def show3(request):
    return HttpResponse('<h1 align="center">Welcome to Informatics branch3</h1>')

def show4(request):
    return HttpResponse('<h1 align="center">Welcome to Informatics branch4</h1>')


def show5(request):
    return render(request,'testapp/hny.html')


def show6(request):
    return render(request,'testapp/results.html')




def show7(request):
    return render(request,'testapp/result1.html')
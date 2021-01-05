from django.shortcuts import render
from django.http import HttpResponse
from newsapp.models import Employee

# Create your views here.



def display(request):
    return render(request,'newsapp/result.html')

def emp_info(request):
    employees=Employee.objects.all()
    return render(request,'newsapp/fetch.html',{'empl':employees})
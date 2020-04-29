from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.
from django.http import HttpResponse
# Create your views here.
def home_view(request ,*args, **kwargs):
 		##return HttpResponse("<H1> This is Home Page for Netflix </H1>")

 		return render(request, "home.html" , {})


def selection_view(request ,*args, **kwargs):
 		##return HttpResponse("<H1> This is Home Page for Netflix </H1>")

 		return render(request, "Selection.html" , {})


from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def test(request) :
    
    return HttpResponse("hello")

def first_Screen(request) :
    return render(
        request,
        "mini2app/first.html",
        {}
    )

def songpa(request):
    return render(
        request,
        "mini2app/songpa.html",
        {}
    )
    
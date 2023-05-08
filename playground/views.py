from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path, include
from django.contrib.auth.models import User
from django.http import JsonResponse


def location(request):
    # This is an http response
    return HttpResponse("Location: USA")


def say_hello(request):
   # This is a JSON example
    return JsonResponse({"name":"Matt"})

def say_goodbye(request):
    # This is a template example for an html file
    return render(request, "goodbye.html",{"name":"Matt"})

   

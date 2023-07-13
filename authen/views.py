from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def handle_login(request):
    return HttpResponse("this is login page")

def handle_logout(request):
    return HttpResponse("this is logout page")

def signup(request):
    return HttpResponse("this is signup page")
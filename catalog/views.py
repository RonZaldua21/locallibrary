from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import path
from . import views


def home(request):
    return HttpResponse("Hello World")
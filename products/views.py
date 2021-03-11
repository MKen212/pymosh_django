from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello World!")


def new(request):
    return HttpResponse("Form for creating a new product!")
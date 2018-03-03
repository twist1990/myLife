from django.shortcuts import render
from django.http import HttpResponse

def firstWord(request):
	return HttpResponse("Hello Ilya, welcome back")

# Create your views here.

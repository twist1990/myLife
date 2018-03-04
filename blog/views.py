from django.shortcuts import render
from django.http import HttpResponse

def firstWord(request):
	return render(request, 'blog/firstWord.html', {})

# Create your views here.

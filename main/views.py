from django.shortcuts import render
from django.http import HttpResponse

from main.models import Match

def home(request):
	context = {}
	return render(request, 'main/login.html', context)
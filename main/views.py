from django.shortcuts import render
from django.http import HttpResponse

from main.models import Match

def home(request):
	match_list = Match.objects.order_by('datetime')
	context = {'match_list': match_list}
	return render(request, 'main/matches.html', context)
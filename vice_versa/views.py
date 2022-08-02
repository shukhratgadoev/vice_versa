from django.http import HttpResponse
from django.shortcuts import render



def about(request):
	return HttpResponse('This is About page')



def home(request):
	return render(request, 'home.html', {'name': 'Shuha'})
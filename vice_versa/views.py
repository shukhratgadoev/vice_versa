from django.http import HttpResponse
from django.shortcuts import render



def about(request):
	return HttpResponse('This is About page')



def home(request):
	return render(request, 'home.html', {'name': 'Shuha'})



def reverse(request):
	user_message = request.GET['message']
	reverser_user_message = user_message[::-1]
	count_user_message = len(user_message)
	
	return render(request, 'reverse.html', {'userMessage': user_message,'reverserUserMessage': reverser_user_message, 'countUserMessage': count_user_message})
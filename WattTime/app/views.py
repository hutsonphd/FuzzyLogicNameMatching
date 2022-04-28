from django.contrib import messages
from django.http import JsonResponse

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout

import app.name_matches as name_matches
from .models import *


#homepage view
@login_required(login_url='Login')
def index(request):
	mappings = Mapping.objects.all()
	context = {
		"mappings":mappings,
	}
	return render(request, 'index.html', context)

@login_required(login_url='Login')
def reset(request):
	name_matches.reset()
	messages.success(request, 'You have reset the Mappings and Entso Data')
	return redirect('app:home')

#file upload page
@login_required(login_url='Login')
def upload(request):
	context = {}	
	return render(request, 'upload.html', context)

#test page
@login_required(login_url='Login')
def test(request):
	result = {}
	result['results'] = name_matches.mapPlatts()
	return JsonResponse(result, safe=False)

#app authentication functions
def loginPage(request):
	nxt = request.GET.get('next')
	if not nxt:
		path_chunks = request.path.split("/")
		nxt = path_chunks[0]
	if request.user.is_authenticated:
		return redirect(nxt, 'app:home')
	else:
		context = {}
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('app:home')
			else:
				messages.info(request, 'Username or Password is incorrect')

	return render(request, 'registration/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('Login')




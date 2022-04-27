from django.http import JsonResponse
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.

@login_required(login_url='Login')
def index(request):
    context = {}
    return render(request, 'index.html', context)

@login_required(login_url='Login')
def api(request):
    response = None
    return JsonResponse(response, safe=False)

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
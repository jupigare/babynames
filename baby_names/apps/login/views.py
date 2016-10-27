from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
	return render(request, 'login/index.html')

def register(request):
	result = User.objects.register(request.POST['user'], request.POST['passw'], request.POST['confirm'])
	if result[0]:
		request.session['id'] = result[1].id
		print request.session['id']
		return redirect('/')
	else:
		for error in result[1]:
			messages.error(request, error)
	return redirect('/loginRegistration')

def login(request):
	result = User.objects.login(request.POST['user'], request.POST['password'])
	if result[0]:
		request.session['id'] = result[1].id
		return redirect('/')
	else:
		for error in result[1]:
			messages.error(request, error)
	return redirect('/loginRegistration')

def home(request):
	return render(request, 'login/home.html')

def logout(request):
	request.session.flush()
	return redirect('/')
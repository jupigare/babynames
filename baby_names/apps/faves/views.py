from django.shortcuts import render, redirect, reverse
from ..login.models import User
from twython import Twython, TwythonError
from django.contrib import messages
from .models import Frequency
from .models import Favorites, Newnames

t = Twython(
	'SWiUdCQsxyRe2uJ32Iq26L9bj',
	'z5bggykXFGKGPbnoXQVOg4kXJuXFbauNnc5Qd7aISoKs72hGxm'
	)

def index(request):
	names = Frequency.objects.all()
	user = User.objects.get(id = request.session['id'])	
	userlist = Favorites.objects.filter(user_id = request.session['id'])
	newnames = Newnames.objects.filter(user_id = request.session['id'])
	context = {'user':user, 'userlist': userlist, 'names':names, 'newnames':newnames}
	return render(request, 'faves/index.html', context)

def addfav(request, id):
	name_id = id
	print name_id
	user = User.objects.get(id = request.session['id'])	
	userlist = Frequency.objects.get(id = name_id)
	Favorites.objects.create(user_id = user, frequency_id = userlist)
	return redirect(reverse('faves:index'))

def delfav(request, id):
	name_id = id
	user = User.objects.get(id = request.session['id'])	
	userlist = Frequency.objects.get(id = name_id)
	Favorites.objects.filter(user_id = user).filter(frequency_id = userlist).delete()
	return redirect(reverse('faves:index'))

def newname(request):
	userlist = Favorites.objects.filter(user_id=request.session['id'])	
	newName = request.POST['newname'][0].upper() + request.POST['newname'][1:].lower()
	newName = newName.encode()
	checknames = []
	if len(request.POST['newname']) < 1:
		messages.error(request, "Please enter a name to")
	for name in userlist:
		checknames.append(name.frequency_id.name)
	if newName in checknames:
		messages.error(request, "Error: Name "+newName+" already in Favorites.")
		return redirect(reverse('faves:index'))
	else:
		pass
		# if Newnames.objects.filter(name = newName).exists():
		# 	messages.error(request, "Error: Name "+newName+" already in Favorites.")
			# return redirect(reverse('faves:index'))
		user = User.objects.get(id = request.session['id'])
		Newnames.objects.create(user_id = user, name = newName)
		return redirect(reverse('faves:index'))

def delnew(request, id):
	name_id = id
	user = User.objects.get(id = request.session['id'])	
	Newnames.objects.filter(user_id = user).filter(id = name_id).delete()
	return redirect(reverse('faves:index'))

from django.shortcuts import render, redirect, reverse
from ..login.models import User
from .models import Frequency, Favorites
from twython import Twython, TwythonError

t = Twython(
	'SWiUdCQsxyRe2uJ32Iq26L9bj',
	'z5bggykXFGKGPbnoXQVOg4kXJuXFbauNnc5Qd7aISoKs72hGxm'
	)

def index(request):
	# if 'freqid' in request.session:
	# 	favorite = Favorites.objects.filter(user_id = request.session['id'])
	names = Frequency.objects.all()
	user = User.objects.get(id = request.session['id'])	
	userlist = Favorites.objects.filter(user_id = request.session['id'])
	context = {'user':user, 'userlist': userlist, 'names':names}
	return render(request, 'faves/index.html', context)

def addfav(request, id):
	# request.session['freqid'] = id
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
from django.shortcuts import render, redirect, reverse
from .models import Frequency, Favorites
from ..login.models import User
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
	results = t.search(q="#babynamesdaily", count = 10)
	all_tweets = results['statuses']
	allTweets=[]
	for tw in all_tweets:
		eachTweet = tw['text'].split('\n')
		temp = []
		for i in eachTweet:
			i = i.encode()
			temp2=i.split(':')
			if temp2 == ['Gender', ' GIRL']:
				temp2 = ['Gender', 'Female']
			elif temp2 == ['Gender', ' BOY']:
				temp2 = ['Gender', 'Male']
			temp.append(temp2)
		allTweets.append([temp[0][1].strip(),temp[1][1].strip(),temp[2][1],temp[3][1]])
	print allTweets
	context = {'user':user, 'userlist': userlist, 'names':names, 'all_tweets':allTweets}
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
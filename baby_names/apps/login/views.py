from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.core.urlresolvers import reverse
from twython import Twython, TwythonError

t = Twython(
	'SWiUdCQsxyRe2uJ32Iq26L9bj',
	'z5bggykXFGKGPbnoXQVOg4kXJuXFbauNnc5Qd7aISoKs72hGxm'
	)

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
		request.session['username'] = result[1].username
		return redirect('/')
	else:
		for error in result[1]:
			messages.error(request, error)
	return redirect('/loginRegistration')

def home(request):
	# results = t.search(q="#babynamesdaily", count = 10)
	# all_tweets = results['statuses']
	# allTweets=[]
	# for tw in all_tweets:
	# 	eachTweet = tw['text'].split('\n')
	# 	temp = []
	# 	for i in eachTweet:
	# 		i = i.encode()
	# 		temp2=i.split(':')
	# 		if temp2 == ['Gender', ' GIRL']:
	# 			temp2 = ['Gender', 'Female']
	# 		elif temp2 == ['Gender', ' BOY']:
	# 			temp2 = ['Gender', 'Male']
	# 		temp.append(temp2)
	# 	allTweets.append([temp[0][1].strip(),temp[1][1].strip(),temp[2][1],temp[3][1]])
	# context = {'all_tweets':allTweets}
	return render(request, 'login/home.html')

def logout(request):
	request.session.flush()
	return redirect('/')
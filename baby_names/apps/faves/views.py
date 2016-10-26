from django.shortcuts import render, redirect
from .models import Frequency, Favorites
from ..login.models import User

# Create your views here.
def index(request):
	if 'freqid' in request.session:
		favorite = Favorites.objects.filter(user_id = id)
	user = User.objects.get(id = request.session['id'])	
	userlist = Frequency.objects.filter()
	context = {'user':user}
	return render(request, 'faves/index.html')

def addfav(request, id):
	request.session['freqid'] = id
	user = User.objects.get(user_id = request.session['id'])	
	userlist = Frequency.objects.get(frequency_id = id)
	Favorites.objects.create(user_id = user, frequency_id = userlist)
	return redirect('/')
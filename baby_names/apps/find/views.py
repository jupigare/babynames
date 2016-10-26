from django.shortcuts import render, redirect, reverse
from django.urls import reverse
from ..faves.models import Frequency, Favorites

def index(request):
	if 'nameSearch' in request.session:
		query = "select id, name, year from frequency where name=%s group by year, name"
		name = {request.session['nameSearch']}
		results = Frequency.objects.raw(query,name)
		try :
			results[0]
		except IndexError:
			del request.session['nameSearch']
		context = {
			'names' : results
		}
	else:
		context = {
			'names' : [{'id':0}]
		}
	if 'id' in request.session:
		faveNames = []
		faveList = Favorites.objects.filter(user_id=request.session['id'])
		for n in faveList:
			faveNames.append(n.frequency_id.name)
		context['faveNames']=faveNames
	return render(request, 'find/index.html', context)
	
def find(request,name):
	if request.method == "POST":
		name = request.POST['nameSearch']
	request.session['nameSearch'] = name[0].upper() + name[1:].lower()
	return redirect(reverse('find:index'))

def reset(request):
	del request.session['nameSearch']
	return redirect(reverse('find:index'))

# Create your views here.
# def index(request):
#    return render(request, 'find/index.html')

# def find(request):
# 	if request.method == "POST":
# 		print("find")
# 		nameSearch = request.POST['nameSearch']
# 		results = Frequency.objects.filter(name=nameSearch)
# 		print(results)
# 		for r in results:
# 			print r.name, r.id
# 		return nameResults(request, nameSearch, results)
# 		# return render(request, 'find/find.html', context)
		
# def nameResults(request, nameSearch, names):
# 	print("nameResults")
# 	print(names)
# 	request.session['nameSearch']=nameSearch
# 	context = {
# 		'year': 2000,
# 		'count': 1
# 	}
# 	return render(request, 'find/index.html', context)

# def addfav(request, id):
# 	# request.session['freqid'] = id
# 	name_id = id
# 	print name_id
# 	user = User.objects.get(id = request.session['id'])	
# 	userlist = Frequency.objects.get(id = name_id)
# 	Favorites.objects.create(user_id = user, frequency_id = userlist)
# 	return redirect(reverse('faves:index'))

# def delfav(request, id):
# 	name_id = id
# 	user = User.objects.get(id = request.session['id'])	
# 	userlist = Frequency.objects.get(id = name_id)
# 	Favorites.objects.filter(user_id = user).filter(frequency_id = userlist).delete()
# 	return redirect(reverse('faves:index'))
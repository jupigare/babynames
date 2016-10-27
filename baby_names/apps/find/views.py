from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.views.generic import View
from ..faves.models import Frequency, Favorites

class Index(View):
	def get(self, request):
		return render(request, 'find/index.html')
	
class Find(View):
	def get(self, request, name):
		request.session['nameSearch'] = name[0].upper() + name[1:].lower()
		return redirect(reverse('find:results', kwargs={'name': name}))
	def post(self, request, name):
		name = request.POST['nameSearch']
		request.session['nameSearch'] = name[0].upper() + name[1:].lower()
		return redirect(reverse('find:results', kwargs={'name': name}))

class Results(View):
	def get(self, request, name):
		query = "select id, name, year, sum(count) as count from frequency where name=%s group by year, name"
		name = {request.session['nameSearch']}
		results = Frequency.objects.raw(query,name)
		try :
			results[0]
		except IndexError:
			messages.error(request, 'Sorry, name '+request.session['nameSearch']+' was not found.', extra_tags='find')
			del request.session['nameSearch']
			pass
		total = 0
		for r in results:
			total += int(r.count)
		context = {
			'names' : results,
			'total' : total
		}
		if 'id' in request.session:
			faveNames = []
			faveList = Favorites.objects.filter(user_id=request.session['id'])
			for n in faveList:
				faveNames.append(n.frequency_id.name)
			context['faveNames']=faveNames
		return render(request, 'find/results.html', context)

class Reset(View):
	def get(self, request):
		if 'nameSearch' in request.session:
			del request.session['nameSearch']
			request.session['nameSearch'].clear()
		return redirect(reverse('find:index'))
	def post(self, request):
		if 'nameSearch' in request.session:
			del request.session['nameSearch']
			request.session['nameSearch'].clear()
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
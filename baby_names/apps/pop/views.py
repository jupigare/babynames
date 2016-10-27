from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from ..faves.models import Frequency, Favorites

class Index(View):
	def get(self, request):
		faveNames = []
		if 'query' not in request.session:
			request.session['query'] = "SELECT id as id, name, FORMAT(sum(count), 0) as count FROM frequency GROUP BY name ORDER BY sum(count) desc"
			request.session['name_dict'] = []
			request.session['genderFilter'] = 'both'
			request.session['stateFilter'] = 'every'
			request.session['yearFilter'] = 'all'
		if 'id' in request.session:
			faveList = Favorites.objects.filter(user_id=request.session['id'])
			for n in faveList:
				faveNames.append(n.frequency_id.name)
		names = Frequency.objects.raw(request.session['query'], request.session['name_dict'])[:100]
		states = Frequency.objects.raw("select distinct state as id, state from frequency order by state")
		years = []
		for i in range(1910,2016):
			years.append(i)
		context = {
			'names': names,
			'faveNames': faveNames,
			'states': states,
			'years': years
		}
		return render(request, 'pop/index.html', context)

class Filter(View):
	def get(self, request):
		print "Running filter..."
		query = "SELECT id as id, name, FORMAT(sum(count), 0) as count FROM frequency"
		whereclause = " WHERE id>0"
		groupby = " GROUP BY name ORDER BY sum(count) desc"
		name_dict = []


		if request.GET['submit']=="Filter":
			
			##### Gender Filter #####
			if 'gender' in request.GET and request.GET['gender']!="":
				request.session['genderFilter'] = request.GET['gender']
				whereclause += " and gender=%s"
				name_dict.append(request.GET['gender'])
			else:
				request.session['genderFilter'] = 'both'

			##### State Filter #####
			if request.GET['state']!="":
				request.session['stateFilter'] = request.GET['state']
				whereclause += " and state=%s"
				name_dict.append(request.GET['state'])
			else:
				request.session['stateFilter'] = 'every'


			##### Year Filters #####
			if 'year' not in request.GET and request.GET['year']=="" and 'yearStart' not in request.GET and 'yearEnd' not in request.GET:
				request.session['yearFilter'] = 'all'
			elif int(request.GET['year'])>=1910 and int(request.GET['year'])<=2015:
				request.session['yearFilter'] = request.GET['year']
				whereclause += " and year=%s"
				name_dict.append(request.GET['year'])
			else:
				if 'yearStart' in request.GET:
					request.session['yearFilter'] = "from "+request.GET['yearStart']+" to "
					whereclause += " and year>=%s"
					name_dict.append(request.GET['yearStart'])
				else:
					request.session['yearFilter'] = "from 1910 to "
				if 'yearEnd' in request.GET:
					request.session['yearFilter'] = request.GET['yearEnd']
					whereclause += " year<=%s"
					name_dict.append(request.GET['yearEnd'])
				else:
					request.session['yearFilter'] = "2015"

			query+=whereclause+groupby
			request.session['query'] = query
			request.session['name_dict'] = name_dict
		elif 'query' in request.session and request.GET['submit']=="Reset":
			del request.session['query']

		return redirect('/popular')
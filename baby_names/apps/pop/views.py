from django.shortcuts import render, redirect, reverse
from ..login.models import User
from django.contrib import messages
from django.views.generic import View
from ..faves.models import Frequency, Favorites

def is_number(something):
	return True

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
			if 'yearStart' in request.GET and 'yearEnd' in request.GET and request.GET['yearStart']>request.GET['yearEnd']:
				messages.error(request, 'Invalid year range entered.', extra_tags='pop')
			elif request.GET['yearStart']!="" or request.GET['yearEnd']!="":
				if 'yearStart' in request.GET and request.GET['yearStart']!="":
					request.session['yearFilter'] = "from "+request.GET['yearStart']+" to "
					whereclause += " and year>=%s"
					name_dict.append(int(request.GET['yearStart']))
				else:
					request.session['yearFilter'] = "from 1910 to "
					whereclause += " and year>=%s"
					name_dict.append('1910')
				if 'yearEnd' in request.GET and request.GET['yearEnd']!="":
					request.session['yearFilter'] += request.GET['yearEnd']
					whereclause += " and year<=%s"
					name_dict.append(int(request.GET['yearEnd']))
				else:
					request.session['yearFilter'] += "2015"
					whereclause += " and year<=%s"
					name_dict.append('2015')
			elif 'year' not in request.GET and request.GET['year']=="" and request.GET['yearStart']=="" and request.GET['yearEnd']=="":
				request.session['yearFilter'] = 'all'
			elif request.GET['year'].isnumeric() and request.GET['year'].isnumeric():
				if int(request.GET['year'])>=1910 and int(request.GET['year'])<=2015:
					request.session['yearFilter'] = request.GET['year']
					whereclause += " and year=%s"
					name_dict.append(request.GET['year'])
			else:
				messages.error(request, 'Invalid year entered.', extra_tags='pop')

			query+=whereclause+groupby
			request.session['query'] = query
			request.session['name_dict'] = name_dict
		elif 'query' in request.session and request.GET['submit']=="Reset":
			del request.session['query']

		return redirect('/popular')

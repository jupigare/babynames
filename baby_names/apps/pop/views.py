from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from ..faves.models import Frequency

class Index(View):
	def get(self, request):
		if 'query' not in request.session:
			request.session['query'] = "SELECT id as id, name, FORMAT(sum(count), 0) as count FROM frequency GROUP BY name ORDER BY sum(count) desc"
			request.session['name_dict'] = []
			request.session['genderFilter'] = 'both'
			request.session['stateFilter'] = 'every'
			request.session['yearFilter'] = 'all'
		names = Frequency.objects.raw(request.session['query'], request.session['name_dict'])[:100]
		states = Frequency.objects.raw("select distinct state as id, state from frequency order by state")
		context = {
			'names': names,
			'states': states
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
			if 'gender' in request.GET and request.GET['gender']!="":
				request.session['genderFilter'] = request.GET['gender']
				whereclause += " and gender=%s"
				name_dict.append(request.GET['gender'])
			else:
				request.session['genderFilter'] = 'both'

			if request.GET['state']!="":
				request.session['stateFilter'] = request.GET['state']
				whereclause += " and state=%s"
				name_dict.append(request.GET['state'])
			else:
				request.session['stateFilter'] = 'every'


			if 'year' not in request.GET or request.GET['year']=="":
				pass
			elif int(request.GET['year'])>=1910 and int(request.GET['year'])<=2015:
				request.session['yearFilter'] = request.GET['year']
				whereclause += " and year=%s"
				name_dict.append(request.GET['year'])
			else:
				request.session['yearFilter'] = 'all'
				print "Invalid year."
			query+=whereclause+groupby
			request.session['query'] = query
			request.session['name_dict'] = name_dict
		elif request.GET['submit']=="Filter":
			del request.session['query']

		return redirect('/popular')
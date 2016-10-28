from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from ..login.models import User
from django.views.generic import View
from bokeh.plotting import figure, ColumnDataSource
from bokeh.resources import CDN
from bokeh.models import Title, HoverTool
from bokeh.embed import components
from ..faves.models import Frequency, Favorites

class Index(View):
	def get(self, request):
		return render(request, 'find/index.html')
	
class Find(View):
	def get(self, request, name):
		request.session['nameSearch'] = name[0].upper() + name[1:].lower()
		return redirect(reverse('find:results', kwargs={'name': name}))
	def post(self, request, name):
		if 'nameSearch' in request.POST and request.POST['nameSearch'] != "":
			name = request.POST['nameSearch']
			request.session['nameSearch'] = name[0].upper() + name[1:].lower()
			return redirect(reverse('find:results', kwargs={'name': name}))
		else:
			messages.error(request, 'Please enter a name to search.', extra_tags='find')
			return redirect(reverse('find:index'))

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
			return redirect(reverse('find:index'))
		total = 0
		year=[]
		count=[]
		for r in results:
			total += int(r.count)
			year.append(r.year)
			count.append(r.count)
		context = {
			'names' : results[0],
			'total' : total
		}

		### Making the Graph ###
		source = ColumnDataSource(
			data=dict(
				# x=x_axis,
				year=year,
				# y=y_axis,
				count=count,
			)
		)
		# hover = HoverTool(tooltips="""
	 #		<table class="tooltips">
	 #			<tr>
	 #				<td>Birth Year</td>
	 #				<td>@year</td>
	 #			</tr>
	 #			<tr>
	 #				<td>Count</td>
	 #				<td>@count</td>
	 #			</tr>
	 #		</table>
	 #		"""
		# )
		p = figure(plot_width=800, plot_height=450, tools=['hover','pan','wheel_zoom','reset','save'], active_drag="pan", active_scroll="wheel_zoom")
		p.line(year,count,source=source, line_width=2)
		hover = p.select(dict(type=HoverTool))
		hover.tooltips = """
			<table class="tooltips">
				<tr>
					<td>Birth Year</td>
					<td>@year</td>
				</tr>
				<tr>
					<td>Count</td>
					<td>@count</td>
				</tr>
			</table>
			"""
		hover.mode = 'mouse'
		p.add_layout(Title(text="Birth Year", align="center"), "below")
		p.add_layout(Title(text="Count", align="center"), "left")
		script, div = components(p, CDN)
		context['bokehScript'] = script
		context['bokehDiv'] = div

		if 'id' in request.session:
			faveNames = []
			faveList = Favorites.objects.filter(user_id=request.session['id'])
			for n in faveList:
				faveNames.append(n.frequency_id.name)
			context['faveNames']=faveNames
		
		return render(request, 'find/graph.html', context)

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
#	return render(request, 'find/index.html')

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

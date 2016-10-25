from django.shortcuts import render
from ..faves.models import Frequency

# Create your views here.
def index(request):
	print "Popular Baby Names page loading..."
	names = Frequency.objects.filter(state="CA",gender="M")[:100]
	newNames = []
	for i in range(0,10):
		newNames.append(names[i])
	context = {
		'names': newNames,
	}
	return render(request, 'pop/index.html', context)
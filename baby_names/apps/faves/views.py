from django.shortcuts import render
from .models import Frequency

# Create your views here.
def index(request):
	hello = Frequency.objects.filter(name ='George')
	print hello[0].name
	pass

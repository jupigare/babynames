from django.shortcuts import render, redirect
from .. faves .models import Frequency
# Create your views here.
#
import random

def index(request):
    return render(request, 'rand/rand.html')

# def length(database):
#     while (database.name !=null):
#         try:
#             count ++
#         except:
#             count = 1
#     return count

def randName(request):
    names = Frequency.objects.filter(gender = request.POST['gender'])
    num = random.randint (0, len(names))
    Rname = names[num].name
    context = {
    'name' : Rname
    }
    return render(request, 'rand/rand.html', context)
     # return redirect(reverse('rand:randName'), context)

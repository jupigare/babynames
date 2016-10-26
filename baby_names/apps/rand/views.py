from django.shortcuts import render, redirect
from .. faves .models import Frequency
# Create your views here.
#
import random
import pdb

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
    if (request.POST['gender'] == '0'):
        names = Frequency.objects.all()

    names = Frequency.objects.filter(gender = request.POST['gender'])
    pdb.set_trace()
    # print request.POST['gender']
    print len(names)
    # default name is empty string
    Rname = ''
    # have names
    if len(names) > 0:
        num = random.randint (0, len(names)-1)
        print num
        Rname = names[num].name

    context = {
        'name' : Rname
    }
    return render(request, 'rand/rand.html', context)
     # return redirect(reverse('rand:randName'), context)

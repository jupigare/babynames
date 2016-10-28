from django.shortcuts import render, redirect
from .. faves .models import Frequency, Favorites
import random

def index(request):
    return render(request, 'rand/rand.html')

def new(request):
    query = "select id, name, gender from frequency"
    if request.method=="GET" or request.POST['gender'] == "0":
        gender=""
    else:
        query += " where gender=%s"
        gender=request.POST['gender']
    query +=  " group by name, gender"
    print query
    results = Frequency.objects.raw(query,(gender))
    names = []
    for i in results:
        names.append(i)
    randNum = random.randint(0, len(names)-1)
    randName = names[randNum]

    context = {
        "name": randName.name,
        "id": randName.id
    }

    if 'id' in request.session:
        faveNames = []
        faveList = Favorites.objects.filter(user_id=request.session['id'])
        for n in faveList:
            faveNames.append(n.frequency_id.name)
        context['faveNames']=faveNames

    return render(request, 'rand/rand.html', context)

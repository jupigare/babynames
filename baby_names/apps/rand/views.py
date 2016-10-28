from django.shortcuts import render, redirect
from ..login.models import User
import random
import pdb
from ..faves.models import Frequency, Favorites

def index(request):
    return render(request, 'rand/rand.html')

# def length(database):
#     while (database.name !=null):
#         try:
#             count ++
#         except:
#             count = 1
#     return count

# def randName(request):
#     if (request.POST['gender'] == '0'):
#         names = Frequency.objects.all()

#     else:
#         names = Frequency.objects.filter(gender = request.POST['gender'])
#     x = len(names)
#     # print request.POST['gender']
#     print "length of name: ",len(names)
#     # default name is empty string


#     # have names
#     if len(names) > 0:
#         num = random.randint (0, len(names))
#         print num
#         Rname = names[num].name

#     context = {
#         'name' : Rname
#     }
#     return render(request, 'rand/rand.html', context)
     # return redirect(reverse('rand:randName'), context)
def new(request):
    # print Frequency._meta.db_table
    # Frequency.objects.raw("select distinct id, name, gender from frequency group by name")
    # query = "SELECT COUNT(*) as id FROM frequency"
    # results = Frequency.objects.raw(query)
    # print results[0].id
    # for i in results:
    #     print i
    #-------------the following are good!!!!$$$$$
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
    # query = "select distinct id, name, gender from frequency group by name"
    # results = Frequency.objects.raw(query)
    # listA = []
    # gender = request.POST['gender']
    # if (gender =='0'):
    #     for i in results:
    #         listA.append(i.name)
    # else:
    #     for i in results:
    #         if i.gender == gender:
    #             listA.append(i.name)

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

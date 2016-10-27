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
def randName(request):
    # print Frequency._meta.db_table
    # Frequency.objects.raw("select distinct id, name, gender from frequency group by name")
    # query = "SELECT COUNT(*) as id FROM frequency"
    # results = Frequency.objects.raw(query)
    # print results[0].id
    # for i in results:
    #     print i
    #-------------the following are good!!!!$$$$$
    query = "select distinct id, name, gender from frequency group by name"
    results = Frequency.objects.raw(query)
    listA = []
    gender = request.POST['gender']
    if (gender =='0'):
        query = "select id, name from frequency"
        results = Frequency.objects.raw(query)
        x = random.randint(0, len(results)-1)
        name = results[x].name
    else:
        query = "select id, name, gender from frequency where gender=" + gender
        results = Frequency.objects.raw(query)
        x = random.randint(0, len(results)-1)
        name = results[x].name

    num = len(listA)
    x = random.randint(0, num-1)
    Rname = listA[x]
    users = Frequency.objects.filter(name = Rname)
    context = {
    "name": Rname,
    "id": users[0].id
    }

    return render(request, 'rand/rand.html', context)

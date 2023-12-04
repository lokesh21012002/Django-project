from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, request, response
from user.models import User

from django.db.models import Q

# Create your views here.


def gettAllUserByExtra(request, id, sub_id):

    request.session["name"] = "lokesh"

    return JsonResponse({"status": 200})

    return JsonResponse({"id": id, "sub_id": sub_id})


def getALlUsers(request, id, username, password):

    s = request.session.get("name")
    print(id, username, password, s)
    # id=request.body['id']
    # result = User.objects.all()  # return all
    result_spec = User.objects.get(pk=id)  # get a specific user based on id
    print(result_spec)

    return JsonResponse({'data': id}, safe=False)


def deleteSession(request):
    del request.session["name"]
    return JsonResponse({"message": "deleted"})


def allUsersOfDb(request):
    username = "Lokesh"
    password = "Lokesh@12345"
    # users = {"users": User.objects.all().values('username', 'password')}
    # print(users.query)
    # users = User.objects.filter(username="Lokesh")
    # users = User.objects.exclude(username="Lokesh")
    # return JsonResponse(list(users), safe=False)

    # users = User.objects.all().order_by('username').values('username', 'password') Ascending
    users = User.objects.all().order_by('username').reverse().values(
        'username', 'password')  # Descending
    # users = User.objects.all().order_by('?').values('username', 'password') Randomly

    # users=User.objects.using('default').all()
    users = User.objects.filter(
        username=username) & User.objects.filter(password=password)
    users = User.objects.filter(username=username, password=password)
    users = User.objects.filter(
        username=username) | User.objects.filter(password=password)
    user = User.objects(Q(username=username) & Q(
        password=password))  # Q object

    return JsonResponse(list(users), safe=False)


# def hello(request):

#     # print(request)
#     a = "Hello World from user"
#     return HttpResponse(f'{a}')


# def name(request):
#     print(type(request))

#     return JsonResponse({'text': "Lokesh Gawande", 'response': 200})


# def dynamic(request):

#     # if request.method == 'GET':
#     #     data = {'name': 'lokesh', 'age': 35}
#     #     return JsonResponse(data)

#     return JsonResponse({"status": 200})

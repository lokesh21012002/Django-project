from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, request, response
from user.models import User

from django.db.models import *

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
    # users = User.objects.all().order_by('username').reverse().values(
    #     'username', 'password')  # Descending
    # users = User.objects.all().order_by('?').values('username', 'password') Randomly

    # users=User.objects.using('default').all()
    # users = User.objects.filter(
    #     username=username) & User.objects.filter(password=password)
    # users = User.objects.filter(username=username, password=password)
    # users = User.objects.filter(
    #     username=username) | User.objects.filter(password=password)
    # user = User.objects(Q(username=username) & Q(
    #     password=password))  # Q object

    # user = User.objects.get(pk=1)
    # print(type(user))
    user = User.objects.order_by('?').first()
    user = User.objects.order_by('?').last()
    user = User.objects.filter(username=username, password=password)
    user = User.objects.filter(pk=id).update(
        username=username, password=password)

    user = User.objects.all()
    if user.count() == 0:
        return JsonResponse({"error": "No data found"}, safe=False)
    else:
        return JsonResponse(list(user), safe=False)

    if user.exists():
        print("User found")
        return JsonResponse({"status": 200, "found": "found"})
    else:
        return JsonResponse({"status": 200, "found": "Not found"})

    # return JsonResponse(user, safe=False)


def signup(request, username, password, email, phone):
    try:
        new_user = User(username=username, password=password,
                        email=email, phone=phone)
        new_user.save()
        return JsonResponse({"status": 200, "msg": "Signed up successfully"}, safe=True)
    except Exception as e:
        return JsonResponse({"status": 400, "msg": str(e)}, safe=True)


def signupCreate(request, username, password, email, phone):
    # update_or_create
    # bulk_create(list_of_objects)
    # bulk_update
    # in_bulk
    # count()
    deleted = User.objects.filter(
        username=username, password=password).delete()

    # for d in deleted:
    #     d.delete()

    user, created = User.objects.get_or_create(
        username, password, email, phone)

    if created:
        return JsonResponse({"status": 200, "msg": "Created Successfully"}, safe=True)
    else:
        return JsonResponse({"status": 400, "msg": "Already Exists"}, safe=True)

    try:
        user_prev = User.objects.filter(
            username=username, email=email, phone=phone)

        if user_prev.exists():
            return JsonResponse({"status": 200, "msg": "User Already exists"})

        else:

            new_user = User.objects.create(username, password, email, phone)
            print(new_user)

        return JsonResponse({"status": 200, "msg": "Signed up successfully"}, safe=True)
    except Exception as e:
        return JsonResponse({"status": 400, "msg": str(e)}, safe=True)


def field_look_ups(request):
    # __exact
    # __contains
    # __lt
    # __in
    # __gt
    # __lte
    # __gte
    # __startswith
    # __isstartswith
    # __range
    # __isnull
    user = User.objects.filter(username__exact="Lokesh")
    user = User.objects.filter(username__contains="o")

    if user.exists():
        return HttpResponse("User Found")
    user = User.objects.filter(id__lt=8)
    user = User.objects.filter(username__startswith="Lo")
    user = User.objects.filter(id__range=(1, 10))
    user = User.objects.filter(id__in=[1, 2, 3])
    user = User.objects.filter(id__isnull=False)


def aggregates(request):
    user = User.objects.all()
    avg = user.aggregate(Avg('id'))
    print(avg)

    user = User.objects.all()
    sum = user.aggregate(Sum('id'))
    print(sum)

    user = User.objects.all()
    min = user.aggregate(Min('id'))
    print(min)

    user = User.objects.all()
    max = user.aggregate(Max('id'))
    print(max)

    user = User.objects.all()
    count = user.aggregate(Count('id'))
    print(count)


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

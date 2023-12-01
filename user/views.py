from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, request
from user.models import User

# Create your views here.


def getALlUsers(request):
    # id=request.body['id']
    result = User.objects.all()  # return all
    # result_spec=User.objects.get(pk=id) get a specific user based on id
    print(type(result))

    return JsonResponse({'data': result}, safe=False)


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
